# -------------------------------------------------------
# Copyright (c) [2022] Nadege Lemperiere
# All rights reserved
# -------------------------------------------------------
# Robotframework test suite for module
# -------------------------------------------------------
# Nadège LEMPERIERE, @07 march 2022
# Latest revision: 01 december 2023
# -------------------------------------------------------


*** Settings ***
Documentation   A test case to check multiple repositories creation using module
Library         aws_iac_keywords.terraform
Library         aws_iac_keywords.keepass
Library         aws_iac_keywords.amplify
Library         aws_iac_keywords.cloudfront
Library         aws_iac_keywords.route53
Library         ../keywords/data.py
Library         OperatingSystem

*** Variables ***
${KEEPASS_DATABASE}                 ${vaultdatabase}
${KEEPASS_KEY_ENV}                  ${vault_key_env}
${KEEPASS_PRINCIPAL_KEY_ENTRY}      /aws/aws-principal-access-key
${KEEPASS_PRINCIPAL_USERNAME}       /aws/aws-principal-credentials
${KEEPASS_ACCOUNT}                  /aws/aws-account
${GITHUB_CICD_TOKEN}                /github/github-cicd-access-token
${REGION}                           eu-west-1

*** Test Cases ***
Prepare Environment
    [Documentation]         Retrieve principal credential from database and initialize python tests keywords
    ${keepass_key}          Get Environment Variable          ${KEEPASS_KEY_ENV}
    ${principal_access}     Load Keepass Database Secret      ${KEEPASS_DATABASE}     ${keepass_key}  ${KEEPASS_PRINCIPAL_KEY_ENTRY}    username
    ${principal_secret}     Load Keepass Database Secret      ${KEEPASS_DATABASE}     ${keepass_key}  ${KEEPASS_PRINCIPAL_KEY_ENTRY}    password
    ${principal_name}       Load Keepass Database Secret      ${KEEPASS_DATABASE}     ${keepass_key}  ${KEEPASS_PRINCIPAL_USERNAME}     username
    ${account}              Load Keepass Database Secret      ${KEEPASS_DATABASE}     ${keepass_key}  ${KEEPASS_ACCOUNT}                password
    ${github_token}         Load Keepass Database Secret      ${KEEPASS_DATABASE}     ${keepass_key}  ${GITHUB_CICD_TOKEN}              password
    Initialize Terraform    ${REGION}   ${principal_access}   ${principal_secret}
    Initialize Amplify      None        ${principal_access}   ${principal_secret}    ${REGION}
    Initialize Cloudfront   None        ${principal_access}   ${principal_secret}    ${REGION}
    Initialize Route53      None        ${principal_access}   ${principal_secret}    ${REGION}
    ${TF_PARAMETERS}=       Create Dictionary   access_token=${github_token}  account=${ACCOUNT}    service_principal=${principal_name}
    Set Global Variable     ${TF_PARAMETERS}

Create Simple React Application
    [Documentation]         Create Application And Check That The AWS Infrastructure Match Specifications
    Launch Terraform Deployment                 ${CURDIR}/../data/simple-react    ${TF_PARAMETERS}
    ${states}   Load Terraform States           ${CURDIR}/../data/simple-react
    ${specs}    Load Simple React Test Data     ${states['test']['outputs']['application']['value']}    ${states['test']['outputs']['main']['value']}    ${states['test']['outputs']['develop']['value']}    ${states['test']['outputs']['distribution']['value']}
    Application Shall Exist And Match           ${specs['application']}
    Distribution Shall Exist And Match          ${specs['distribution']}
    [Teardown]  Destroy Terraform Deployment    ${CURDIR}/../data/simple-react    ${TF_PARAMETERS}

Create React Application With Authentication On Develop Url
    [Documentation]         Create Application And Check That The AWS Infrastructure Match Specifications
    Launch Terraform Deployment                 ${CURDIR}/../data/authentication  ${TF_PARAMETERS}
    ${states}   Load Terraform States           ${CURDIR}/../data/authentication
    ${specs}    Load Authentication Test Data   ${states['test']['outputs']['application']['value']}    ${states['test']['outputs']['main']['value']}    ${states['test']['outputs']['develop']['value']}    ${states['test']['outputs']['distribution']['value']}
    Application Shall Exist And Match           ${specs['application']}
    Distribution Shall Exist And Match          ${specs['distribution']}
    [Teardown]  Destroy Terraform Deployment    ${CURDIR}/../data/authentication  ${TF_PARAMETERS}

Create React Application With Logging Capabilities
    [Documentation]         Create Application And Check That The AWS Infrastructure Match Specifications
    Launch Terraform Deployment                 ${CURDIR}/../data/logging  ${TF_PARAMETERS}
    ${states}   Load Terraform States           ${CURDIR}/../data/logging
    ${specs}    Load Logging Test Data          ${states['test']['outputs']['application']['value']}    ${states['test']['outputs']['main']['value']}    ${states['test']['outputs']['develop']['value']}    ${states['test']['outputs']['distribution']['value']}    ${states['test']['outputs']['bucket']['value']}
    Application Shall Exist And Match           ${specs['application']}
    Distribution Shall Exist And Match          ${specs['distribution']}
    [Teardown]  Destroy Terraform Deployment    ${CURDIR}/../data/logging  ${TF_PARAMETERS}

Create React Application With Domain Record
    [Documentation]         Create Application And Check That The AWS Infrastructure Match Specifications
    Launch Terraform Deployment                 ${CURDIR}/../data/domain  ${TF_PARAMETERS}
    ${states}   Load Terraform States           ${CURDIR}/../data/domain
    ${specs}    Load Domain Test Data           ${states['test']['outputs']['application']['value']}    ${states['test']['outputs']['main']['value']}    ${states['test']['outputs']['develop']['value']}    ${states['test']['outputs']['distribution']['value']}    ${states['test']['outputs']['domain_zone']['value']}    ${states['test']['outputs']['certificate']['value']}
    Application Shall Exist And Match           ${specs['application']}
    Distribution Shall Exist And Match          ${specs['distribution']}
    Record Shall Exist And Match                ${specs['record']}
    [Teardown]  Destroy Terraform Deployment    ${CURDIR}/../data/domain  ${TF_PARAMETERS}
