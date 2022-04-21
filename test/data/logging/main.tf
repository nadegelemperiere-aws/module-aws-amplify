# -------------------------------------------------------
# TECHNOGIX
# -------------------------------------------------------
# Copyright (c) [2022] Technogix.io
# All rights reserved
# -------------------------------------------------------
# Simple deployment for repository testing
# -------------------------------------------------------
# Nadège LEMPERIERE, @07 march 2022
# Latest revision: 07 march 2022
# -------------------------------------------------------

# -------------------------------------------------------
# Create the s3 logging bucket
# -------------------------------------------------------
resource "random_string" "random" {
	length		= 32
	special		= false
	upper 		= false
}
resource "aws_s3_bucket" "logging" {
	bucket = random_string.random.result
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
	repository				= "https://github.com/technogix/portal.git"
	framework				= "React"
	access_token			= var.access_token
	env						= { _LIVE_UPDATES = "[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]"}
	logging					= {
		bucket 	= aws_s3_bucket.logging.bucket_domain_name
		prefix 	= "test/"
		cookies = true
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

output "bucket" {
	value = aws_s3_bucket.logging.arn
}