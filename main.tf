# -------------------------------------------------------
# Copyright (c) [2022] Nadege Lemperiere
# All rights reserved
# -------------------------------------------------------
# Module to deploy an ecr repository with all the secure
# components required
# -------------------------------------------------------
# Nadège LEMPERIERE, @07 march 2022
# Latest revision: 07 march 2022
# -------------------------------------------------------

# -------------------------------------------------------
# Create the aws amplify app
# -------------------------------------------------------
resource "aws_amplify_app" "application" {
  	name 					= var.name
	repository 				= var.repository
	build_spec  			= var.build
	access_token 			= var.access_token
  	environment_variables 	= var.env

	dynamic "custom_rule" {
		for_each = ((var.is_spa != null) ? ["once"] : [])
		content {
			source = "</^[^.]+$|\\.(?!(css|gif|ico|jpg|js|png|txt|svg|webp|woff|ttf|map|json)$)([^.]+$)/>"
    		status = "200"
    		target = "/index.html"
		}
  	}

	tags = {
        Name                = "${var.project}.${var.environment}.${var.module}.application.${var.name}"
        Environment         = var.environment
        Owner               = var.email
        Project             = var.project
        Version             = var.git_version
        Module              = var.module
    }
}

# -------------------------------------------------------
# Declare production branch
# -------------------------------------------------------
resource "aws_amplify_branch" "main" {
	app_id      				= aws_amplify_app.application.id
  	branch_name 				= "main"
	description 				= "production branch"
	enable_pull_request_preview = true

  	framework 					= var.framework
  	stage     					= "PRODUCTION"

  	environment_variables 		= var.env

	tags = {
        Name                = "${var.project}.${var.environment}.${var.module}.main.${var.name}"
        Environment         = var.environment
        Owner               = var.email
        Project             = var.project
        Version             = var.git_version
        Module              = var.module
    }
}

resource "aws_amplify_webhook" "main" {
	app_id      = aws_amplify_app.application.id
  	branch_name = aws_amplify_branch.main.branch_name
  	description = "triggermain"
}

# -------------------------------------------------------
# Declare beta branch
# -------------------------------------------------------
resource "aws_amplify_branch" "develop" {
	app_id      				= aws_amplify_app.application.id
  	branch_name 				= "develop"
	description 				= "staging branch"
	enable_auto_build 			= true
	enable_pull_request_preview = true

  	framework 					= var.framework
  	stage     					= "BETA"

  	environment_variables 		= var.env

	enable_basic_auth = ((var.authentication != null) ? true : false)
	basic_auth_credentials = var.authentication

	tags = {
        Name                = "${var.project}.${var.environment}.${var.module}.develop.${var.name}"
        Environment         = var.environment
        Owner               = var.email
        Project             = var.project
        Version             = var.git_version
        Module              = var.module
    }
}

resource "aws_amplify_webhook" "develop" {
	app_id      = aws_amplify_app.application.id
  	branch_name = aws_amplify_branch.develop.branch_name
  	description = "triggerdevelop"
}

# -------------------------------------------------------
# Expose through cloudfront
# -------------------------------------------------------

locals {
	aliases      	= var.domain == null ? [] : [for subd in var.domain.subdomains : ((length(subd) == 0) ? var.domain.name : format("%s.%s",subd,var.domain.name))]
}

resource "aws_cloudfront_distribution" "application" {

	enabled = true
	price_class = "PriceClass_100" # US and Europe optimization only
	web_acl_id = var.acl

	origin {

		origin_id 			   = "${var.name}-main"
		domain_name 		   = "main.${aws_amplify_app.application.default_domain}"

		custom_origin_config {
			http_port 			   = 80
			https_port             = 443
			origin_protocol_policy = "https-only"
    		origin_ssl_protocols   = [ "TLSv1.2" ]
		}
  	}

  	dynamic "logging_config" {
		for_each = ((var.logging != null) ? ["once"] : [])
		content {
			include_cookies = var.logging.cookies
			bucket          = var.logging.bucket
			prefix          = var.logging.prefix
		}
  	}

	dynamic "viewer_certificate" {
		for_each = ((var.domain != null) ? ["once"] : [])
		content {
			acm_certificate_arn = var.domain.certificate
			minimum_protocol_version = "TLSv1.2_2021"
			ssl_support_method = "sni-only"
		}
	}

	dynamic "viewer_certificate" {
		for_each = ((var.domain == null) ? ["once"] : [])
		content {
			cloudfront_default_certificate = true
		}
	}

  	aliases = local.aliases

  	default_cache_behavior {
    	allowed_methods  = ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
    	cached_methods   = ["GET", "HEAD"]
    	target_origin_id = "${var.name}-main"

    	forwarded_values {
     		query_string = false
			cookies {
        		forward = "none"
     		}
    	}

    	viewer_protocol_policy = "https-only"
    	min_ttl                = 0
    	default_ttl            = 3600
    	max_ttl                = 86400
  	}

	restrictions {
		geo_restriction {
			restriction_type = "blacklist"
			locations        = ["CN", "RU"]
		}
	}

	tags = {
        Name                = "${var.project}.${var.environment}.${var.module}.cloudfront.${var.name}"
        Environment         = var.environment
        Owner               = var.email
        Project             = var.project
        Version             = var.git_version
        Module              = var.module
    }
}

# -------------------------------------------------------
# Declare distribution in route53 domain
# -------------------------------------------------------
resource "aws_route53_record" "application" {

	count	= var.domain == null ? 0 : length(var.domain.subdomains)

  	zone_id = var.domain.zone
	name 	= var.domain.subdomains[count.index]
  	type    = (length(var.domain.subdomains[count.index]) > 0) ? "CNAME" : "A"
  	ttl     = (length(var.domain.subdomains[count.index]) > 0) ? "60" : null
  	records = (length(var.domain.subdomains[count.index]) > 0) ? [aws_cloudfront_distribution.application.domain_name] : null
	dynamic "alias" {
		for_each = (length(var.domain.subdomains[count.index]) > 0) ? [] : [ "once" ]
		content {
			name 					= aws_cloudfront_distribution.application.domain_name
			zone_id 				= aws_cloudfront_distribution.application.hosted_zone_id
			evaluate_target_health 	= true
		}
	}
}
