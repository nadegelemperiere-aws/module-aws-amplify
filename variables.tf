# -------------------------------------------------------
# Copyright (c) [2022] Nadege Lemperiere
# All rights reserved
# -------------------------------------------------------
# Module to deploy an ecr repository with all the secure
# components required
# -------------------------------------------------------
# Nadège LEMPERIERE, @07 march 2022
# Latest revision: 30 november 2023
# -------------------------------------------------------

# -------------------------------------------------------
# Contact e-mail for this deployment
# -------------------------------------------------------
variable "email" {
	type 		= string
	nullable    = false
}

# -------------------------------------------------------
# Environment for this deployment (prod, preprod, ...)
# -------------------------------------------------------
variable "environment" {
	type 		= string
	nullable    = false
}

# -------------------------------------------------------
# Topic context for this deployment
# -------------------------------------------------------
variable "project" {
	type    	= string
	nullable    = false
}
variable "module" {
	type 		= string
	nullable    = false
}

# -------------------------------------------------------
# Solution version
# -------------------------------------------------------
variable "git_version" {
	type    	= string
	default 	= "unmanaged"
	nullable    = false
}

# -------------------------------------------------------
# Application name
# -------------------------------------------------------
variable "name" {
	type     	= string
	nullable 	= false
}

# -------------------------------------------------------
# Application building
# -------------------------------------------------------
variable "repository" {
	type     	= string
	nullable 	= false
}
variable "access_token" {
	type     	= string
	sensitive 	= true
}
variable "framework" {
	type     	= string
	nullable 	= false
}
variable "build" {
	type     	= string
	default  	= null
}
variable "env" {
	type     	= map
	default  	= null
}
variable "is_spa" {
	type		= bool
	default		= false
}

# -------------------------------------------------------
# Application domain name
# -------------------------------------------------------
variable "domain" {
	type     	= object({
		name 		= string
		subdomains 	= list(string)
		certificate = string
		zone		= string
	})
	default  	= null

}

# -------------------------------------------------------
# Authentication (base64 encoded user:password) for develop branch
# -------------------------------------------------------
variable "authentication" {
	type 		= string
	default  	= null
}

# -------------------------------------------------------
# Logging configuration
# -------------------------------------------------------
variable "logging" {
	type 		= object({
		bucket 		= string
		prefix 		= string
		cookies		= bool
	})
	default  	= null
}


# -------------------------------------------------------
# WAF configuration
# -------------------------------------------------------
variable "acl" {
	type = string
	default = null
}