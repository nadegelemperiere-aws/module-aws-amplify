# -------------------------------------------------------
# Copyright (c) [2022] Nadege Lemperiere
# All rights reserved
# -------------------------------------------------------
# Module to deploy an ecr repository with all the secure
# components required
# -------------------------------------------------------
# Nadège LEMPERIERE, @12 november 2021
# Latest revision: 12 november 2021
# -------------------------------------------------------

output "application" {
    value = {
        arn         = aws_amplify_app.application.arn
        domain      = aws_amplify_app.application.default_domain
        id          = aws_amplify_app.application.id
        production  = aws_amplify_app.application.production_branch
    }
}

output "main" {
    value = {
        arn         = aws_amplify_branch.main.arn
        resources   = aws_amplify_branch.main.associated_resources
        domains     = aws_amplify_branch.main.custom_domains
        destination = aws_amplify_branch.main.destination_branch
        source      = aws_amplify_branch.main.source_branch
        webhook     = aws_amplify_webhook.main.url
    }
}

output "develop" {
    value = {
        arn         = aws_amplify_branch.develop.arn
        resources   = aws_amplify_branch.develop.associated_resources
        domains     = aws_amplify_branch.develop.custom_domains
        destination = aws_amplify_branch.develop.destination_branch
        source      = aws_amplify_branch.develop.source_branch
        webhook     = aws_amplify_webhook.develop.url
    }
}

output "distribution" {
    value = {
        arn         = aws_cloudfront_distribution.application.arn
        domain      = aws_cloudfront_distribution.application.domain_name
        etag        = aws_cloudfront_distribution.application.etag
        zone        = aws_cloudfront_distribution.application.hosted_zone_id
    }
}