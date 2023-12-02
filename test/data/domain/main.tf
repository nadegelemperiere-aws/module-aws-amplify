# -------------------------------------------------------
# Copyright (c) [2022] Nadege Lemperiere
# All rights reserved
# -------------------------------------------------------
# Simple deployment for repository testing
# -------------------------------------------------------
# Nadège LEMPERIERE, @07 march 2022
# Latest revision: 07 march 2022
# -------------------------------------------------------


# -------------------------------------------------------
# Terraform configuration
# -------------------------------------------------------
provider "aws" {
	alias		= "us"
	region		= "us-east-1"
	access_key 	= var.access_key
	secret_key	= var.secret_key
}

data "aws_acm_certificate" "test" {
  	domain   = "technogix.io"
  	statuses = ["ISSUED"]
	provider = "aws.us"

}

data "aws_route53_zone" "test" {
  	name         = "technogix.io"
  	private_zone = false
}


# -------------------------------------------------------
# Create repositories using the current module
# -------------------------------------------------------
module "application" {

	source 					= "../../../"
	email 					= "moi.moi@moi.fr"
	project 				= "test"
	environment 			= "test"
	module 					= "test"
	git_version 			= "test"
	name 					= "test"
	repository				= "https://github.com/nadegelemperiere/portal.git"
	is_spa					= true
	framework				= "React"
	access_token			= var.access_token
	env						= { _LIVE_UPDATES = "[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]"}
		domain 				= {
		name = "technogix.io"
		subdomains = ["test-module-aws-amplify"]
		certificate = data.aws_acm_certificate.test.arn
		zone = data.aws_route53_zone.test.zone_id
	}
}

# -------------------------------------------------------
# Terraform configuration
# -------------------------------------------------------
provider "aws" {
	region		= var.region
	access_key 	= var.access_key
	secret_key	= var.secret_key
}

terraform {
	required_version = ">=1.0.8"
	backend "local"	{
		path="terraform.tfstate"
	}
}

# -------------------------------------------------------
# AWS credentials
# -------------------------------------------------------
variable "access_key" {
	type    	= string
	sensitive 	= true
}
variable "secret_key" {
	type    	= string
	sensitive 	= true
}
variable "region" {
	type    	= string
}
variable "access_token" {
	type    	= string
	sensitive 	= true
}

# -------------------------------------------------------
# IAM account which root to use
# -------------------------------------------------------
variable "account" {
	type 		= string
	sensitive 	= true
}
variable "service_principal" {
	type 		= string
	sensitive 	= true
}

output "application" {
    value = module.application.application
}

output "main" {
    value = module.application.main
}

output "develop" {
    value = module.application.develop
}

output "distribution" {
    value = module.application.distribution
}

output "domain_zone" {
	value = data.aws_route53_zone.test
}

output "certificate" {
	value = data.aws_acm_certificate.test
}