# -------------------------------------------------------
# Copyright (c) [2022] Nadege Lemperiere
# All rights reserved
# -------------------------------------------------------
# Keywords to create data for module test
# -------------------------------------------------------
# Nadège LEMPERIERE, @13 november 2021
# Latest revision: 01 december 2023
# -------------------------------------------------------

# System includes
from json import load, dumps

# Robotframework includes
from robot.libraries.BuiltIn import BuiltIn, _Misc
from robot.api import logger as logger
from robot.api.deco import keyword
ROBOT = False

# ip address manipulation
from ipaddress import IPv4Network

@keyword('Load Simple React Test Data')
def load_simple_react_test_data(application, main, develop, distribution) :

    result = {}
    result['application'] = []
    result['application'].append({'name' : 'simple-react', 'data' : {}})
    result['application'][0]['data']['appId'] = application['id']
    result['application'][0]['data']['appArn'] = application['arn']
    result['application'][0]['data']['enableBasicAuth'] = False
    result['application'][0]['data']['customRules'] =  [{
        'source': '</^[^.]+$|\\.(?!(css|gif|ico|jpg|js|png|txt|svg|webp|woff|ttf|map|json)$)([^.]+$)/>',
        'target': '/index.html',
        'status': '200'
    }]
    result['application'][0]['data']['name'] = 'test'
    result['application'][0]['data']['repository'] = 'https://github.com/nadegelemperiere/portal.git'
    result['application'][0]['data']['platform'] = 'WEB'
    result['application'][0]['data']['environmentVariables'] = {
        '_LIVE_UPDATES' : '[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]'
    }
    result['application'][0]['data']['defaultDomain'] = application['domain']

    result['application'][0]['data']['branches'] = []
    result['application'][0]['data']['branches'].append(
        {
            'branchArn'             : main['arn'],
            'branchName'            : 'main',
            'framework'             : 'React',
            'stage'                 : 'PRODUCTION',
            'environmentVariables'  : {
                '_LIVE_UPDATES' : '[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]'
            },
            'enableBasicAuth'       : False,
            'tags'                  : {
                'Version'       : 'test',
                'Name'          : 'test.test.test.main.test',
                'Project'       : 'test',
                'Module'        : 'test',
                'Environment'   : 'test',
                'Owner'         : 'moi.moi@moi.fr'
            }
        }
    )
    result['application'][0]['data']['branches'].append(
        {
            'branchArn'             : develop['arn'],
            'branchName'            : 'develop',
            'framework'             : 'React',
            'stage'                 : 'BETA',
            'environmentVariables'  : {
                '_LIVE_UPDATES' : '[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]'
            },
            'enableBasicAuth'       : False,
            'tags'                  : {
                'Version'       : 'test',
                'Name'          : 'test.test.test.develop.test',
                'Project'       : 'test',
                'Module'        : 'test',
                'Environment'   : 'test',
                'Owner'         : 'moi.moi@moi.fr'
            }
        }
    )
    result['application'][0]['data']['webhooks'] = []
    result['application'][0]['data']['webhooks'].append(
        {
            'webhookUrl'             : develop['webhook'],
            'branchName'            : 'develop'
        }
    )
    result['application'][0]['data']['webhooks'].append(
        {
            'webhookUrl'             : main['webhook'],
            'branchName'            : 'main'
        }
    )

    result['application'][0]['data']['tags'] = {}
    result['application'][0]['data']['tags']['Version'] = 'test'
    result['application'][0]['data']['tags']['Project'] = 'test'
    result['application'][0]['data']['tags']['Module']  = 'test'
    result['application'][0]['data']['tags']['Environment'] = 'test'
    result['application'][0]['data']['tags']['Owner'] = 'moi.moi@moi.fr'
    result['application'][0]['data']['tags']['Name'] = 'test.test.test.application.test'

    result['distribution'] = []
    result['distribution'].append({'name' : 'domain', 'data' : {}})
    result['distribution'][0]['data']['ARN'] = distribution['arn']
    result['distribution'][0]['data']['Id'] = distribution['arn'].split('/')[1]
    result['distribution'][0]['data']['Status'] = 'Deployed'
    result['distribution'][0]['data']['DomainName'] = distribution['domain']
    result['distribution'][0]['data']['DistributionConfig'] = {}
    result['distribution'][0]['data']['DistributionConfig']['Aliases'] = {
        'Quantity' : 0
    }
    result['distribution'][0]['data']['DistributionConfig']['Origins'] = {
        'Quantity' : 1,
        'Items' : [{
            'Id' : 'test-main',
            'DomainName': 'main.' + application['domain'],
            'OriginPath': '',
            'CustomHeaders': {
                'Quantity' : 0
            },
            'CustomOriginConfig': {
                'HTTPPort' : 80,
                'HTTPSPort' : 443,
                'OriginProtocolPolicy' : 'https-only',
                'OriginSslProtocols' : {
                    'Quantity' : 1,
                    'Items' : ['TLSv1.2']
                }
            },
        }]
    }
    result['distribution'][0]['data']['DistributionConfig']['DefaultCacheBehavior'] = {
        'TargetOriginId': 'test-main',
        'TrustedSigners': {
            'Enabled': False,
            'Quantity': 0
        },
        'TrustedKeyGroups' : {
            'Enabled': False,
            'Quantity': 0
        },
        'ViewerProtocolPolicy': 'https-only',
        'AllowedMethods': {
            'Quantity': 7,
            'Items': ["HEAD", "DELETE", "POST", "GET", "OPTIONS", "PUT", "PATCH"],
            'CachedMethods': {
                'Quantity': 2,
                'Items': ["HEAD", "GET"]
            }
        },
        'LambdaFunctionAssociations': {
            'Quantity': 0
        },
        'FunctionAssociations': {
            'Quantity': 0
        },
        'DefaultTTL': 3600
    }
    result['distribution'][0]['data']['DistributionConfig']['Logging'] = {
        'Enabled': False,
        'IncludeCookies': False,
        'Bucket': '',
        'Prefix': ''
    }
    result['distribution'][0]['data']['DistributionConfig']['PriceClass'] = 'PriceClass_100'
    result['distribution'][0]['data']['DistributionConfig']['Enabled'] = True
    result['distribution'][0]['data']['DistributionConfig']['ViewerCertificate'] = {
        'CloudFrontDefaultCertificate': True,
        'SSLSupportMethod': 'vip',
        'MinimumProtocolVersion': 'TLSv1',
        'CertificateSource': 'cloudfront'
    }
    result['distribution'][0]['data']['DistributionConfig']['Restrictions'] = {
        'GeoRestriction' : {
            'RestrictionType' : 'blacklist',
            'Quantity' : 2,
            'Items' : [ 'CN', 'RU' ]
        }
    }

    logger.debug(dumps(result))

    return result

@keyword('Load Authentication Test Data')
def load_authentication_test_data(application, main, develop, distribution) :

    result = {}
    result['application'] = []
    result['distribution'] = []
    result['application'].append({'name' : 'authentication', 'data' : {}})
    result['distribution'].append({'name' : 'authentication', 'data' : {}})
    result['application'][0]['data']['appId'] = application['id']
    result['application'][0]['data']['appArn'] = application['arn']
    result['application'][0]['data']['customRules'] =  [{
        'source': '</^[^.]+$|\\.(?!(css|gif|ico|jpg|js|png|txt|svg|webp|woff|ttf|map|json)$)([^.]+$)/>',
        'target': '/index.html',
        'status': '200'
    }]
    result['application'][0]['data']['name'] = 'test'
    result['application'][0]['data']['repository'] = 'https://github.com/nadegelemperiere/portal.git'
    result['application'][0]['data']['platform'] = 'WEB'
    result['application'][0]['data']['environmentVariables'] = {
        '_LIVE_UPDATES' : '[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]'
    }
    result['application'][0]['data']['defaultDomain'] = application['domain']

    result['application'][0]['data']['branches'] = []
    result['application'][0]['data']['branches'].append(
        {
            'branchArn'             : main['arn'],
            'branchName'            : 'main',
            'framework'             : 'React',
            'stage'                 : 'PRODUCTION',
            'environmentVariables'  : {
                '_LIVE_UPDATES' : '[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]'
            },
            'enableBasicAuth'       : False,
            'tags'                  : {
                'Version'       : 'test',
                'Name'          : 'test.test.test.main.test',
                'Project'       : 'test',
                'Module'        : 'test',
                'Environment'   : 'test',
                'Owner'         : 'moi.moi@moi.fr'
            }
        }
    )
    result['application'][0]['data']['branches'].append(
        {
            'branchArn'             : develop['arn'],
            'branchName'            : 'develop',
            'framework'             : 'React',
            'stage'                 : 'BETA',
            'environmentVariables'  : {
                '_LIVE_UPDATES' : '[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]'
            },
            'enableBasicAuth'       : True,
            'tags'                  : {
                'Version'       : 'test',
                'Name'          : 'test.test.test.develop.test',
                'Project'       : 'test',
                'Module'        : 'test',
                'Environment'   : 'test',
                'Owner'         : 'moi.moi@moi.fr'
            }
        }
    )
    result['application'][0]['data']['webhooks'] = []
    result['application'][0]['data']['webhooks'].append(
        {
            'webhookUrl'             : develop['webhook'],
            'branchName'            : 'develop'
        }
    )
    result['application'][0]['data']['webhooks'].append(
        {
            'webhookUrl'             : main['webhook'],
            'branchName'            : 'main'
        }
    )

    result['application'][0]['data']['tags'] = {}
    result['application'][0]['data']['tags']['Version'] = 'test'
    result['application'][0]['data']['tags']['Project'] = 'test'
    result['application'][0]['data']['tags']['Module']  = 'test'
    result['application'][0]['data']['tags']['Environment'] = 'test'
    result['application'][0]['data']['tags']['Owner'] = 'moi.moi@moi.fr'
    result['application'][0]['data']['tags']['Name'] = 'test.test.test.application.test'


    result['distribution'] = []
    result['distribution'].append({'name' : 'domain', 'data' : {}})
    result['distribution'][0]['data']['ARN'] = distribution['arn']
    result['distribution'][0]['data']['Id'] = distribution['arn'].split('/')[1]
    result['distribution'][0]['data']['Status'] = 'Deployed'
    result['distribution'][0]['data']['DomainName'] = distribution['domain']
    result['distribution'][0]['data']['DistributionConfig'] = {}
    result['distribution'][0]['data']['DistributionConfig']['Aliases'] = {
        'Quantity' : 0
    }
    result['distribution'][0]['data']['DistributionConfig']['Origins'] = {
        'Quantity' : 1,
        'Items' : [{
            'Id' : 'test-main',
            'DomainName': 'main.' + application['domain'],
            'OriginPath': '',
            'CustomHeaders': {
                'Quantity' : 0
            },
            'CustomOriginConfig': {
                'HTTPPort' : 80,
                'HTTPSPort' : 443,
                'OriginProtocolPolicy' : 'https-only',
                'OriginSslProtocols' : {
                    'Quantity' : 1,
                    'Items' : ['TLSv1.2']
                }
            },
        }]
    }
    result['distribution'][0]['data']['DistributionConfig']['DefaultCacheBehavior'] = {
        'TargetOriginId': 'test-main',
        'TrustedSigners': {
            'Enabled': False,
            'Quantity': 0
        },
        'TrustedKeyGroups' : {
            'Enabled': False,
            'Quantity': 0
        },
        'ViewerProtocolPolicy': 'https-only',
        'AllowedMethods': {
            'Quantity': 7,
            'Items': ["HEAD", "DELETE", "POST", "GET", "OPTIONS", "PUT", "PATCH"],
            'CachedMethods': {
                'Quantity': 2,
                'Items': ["HEAD", "GET"]
            }
        },
        'LambdaFunctionAssociations': {
            'Quantity': 0
        },
        'FunctionAssociations': {
            'Quantity': 0
        },
        'DefaultTTL': 3600
    }
    result['distribution'][0]['data']['DistributionConfig']['Logging'] = {
        'Enabled': False,
        'IncludeCookies': False,
        'Bucket': '',
        'Prefix': ''
    }
    result['distribution'][0]['data']['DistributionConfig']['PriceClass'] = 'PriceClass_100'
    result['distribution'][0]['data']['DistributionConfig']['Enabled'] = True
    result['distribution'][0]['data']['DistributionConfig']['ViewerCertificate'] = {
        'CloudFrontDefaultCertificate': True,
        'SSLSupportMethod': 'vip',
        'MinimumProtocolVersion': 'TLSv1',
        'CertificateSource': 'cloudfront'
    }
    result['distribution'][0]['data']['DistributionConfig']['Restrictions'] = {
        'GeoRestriction' : {
            'RestrictionType' : 'blacklist',
            'Quantity' : 2,
            'Items' : [ 'CN', 'RU' ]
        }
    }


    logger.debug(dumps(result))

    return result


@keyword('Load Logging Test Data')
def load_logging_test_data(application, main, develop, distribution, bucket) :

    result = {}
    result['application'] = []
    result['distribution'] = []
    result['application'].append({'name' : 'logging', 'data' : {}})
    result['distribution'].append({'name' : 'logging', 'data' : {}})
    result['application'][0]['data']['appId'] = application['id']
    result['application'][0]['data']['appArn'] = application['arn']
    result['application'][0]['data']['customRules'] =  [{
        'source': '</^[^.]+$|\\.(?!(css|gif|ico|jpg|js|png|txt|svg|webp|woff|ttf|map|json)$)([^.]+$)/>',
        'target': '/index.html',
        'status': '200'
    }]
    result['application'][0]['data']['enableBasicAuth'] = False
    result['application'][0]['data']['name'] = 'test'
    result['application'][0]['data']['repository'] = 'https://github.com/nadegelemperiere/portal.git'
    result['application'][0]['data']['platform'] = 'WEB'
    result['application'][0]['data']['environmentVariables'] = {
        '_LIVE_UPDATES' : '[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]'
    }
    result['application'][0]['data']['defaultDomain'] = application['domain']

    result['application'][0]['data']['branches'] = []
    result['application'][0]['data']['branches'].append(
        {
            'branchArn'             : main['arn'],
            'branchName'            : 'main',
            'framework'             : 'React',
            'stage'                 : 'PRODUCTION',
            'environmentVariables'  : {
                '_LIVE_UPDATES' : '[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]'
            },
            'enableBasicAuth'       : False,
            'tags'                  : {
                'Version'       : 'test',
                'Name'          : 'test.test.test.main.test',
                'Project'       : 'test',
                'Module'        : 'test',
                'Environment'   : 'test',
                'Owner'         : 'moi.moi@moi.fr'
            }
        }
    )
    result['application'][0]['data']['branches'].append(
        {
            'branchArn'             : develop['arn'],
            'branchName'            : 'develop',
            'framework'             : 'React',
            'stage'                 : 'BETA',
            'environmentVariables'  : {
                '_LIVE_UPDATES' : '[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]'
            },
            'enableBasicAuth'       : False,
            'tags'                  : {
                'Version'       : 'test',
                'Name'          : 'test.test.test.develop.test',
                'Project'       : 'test',
                'Module'        : 'test',
                'Environment'   : 'test',
                'Owner'         : 'moi.moi@moi.fr'
            }
        }
    )
    result['application'][0]['data']['webhooks'] = []
    result['application'][0]['data']['webhooks'].append(
        {
            'webhookUrl'             : develop['webhook'],
            'branchName'            : 'develop'
        }
    )
    result['application'][0]['data']['webhooks'].append(
        {
            'webhookUrl'             : main['webhook'],
            'branchName'            : 'main'
        }
    )

    result['application'][0]['data']['tags'] = {}
    result['application'][0]['data']['tags']['Version'] = 'test'
    result['application'][0]['data']['tags']['Project'] = 'test'
    result['application'][0]['data']['tags']['Module']  = 'test'
    result['application'][0]['data']['tags']['Environment'] = 'test'
    result['application'][0]['data']['tags']['Owner'] = 'moi.moi@moi.fr'
    result['application'][0]['data']['tags']['Name'] = 'test.test.test.application.test'


    result['distribution'] = []
    result['distribution'].append({'name' : 'domain', 'data' : {}})
    result['distribution'][0]['data']['ARN'] = distribution['arn']
    result['distribution'][0]['data']['Id'] = distribution['arn'].split('/')[1]
    result['distribution'][0]['data']['Status'] = 'Deployed'
    result['distribution'][0]['data']['DomainName'] = distribution['domain']
    result['distribution'][0]['data']['DistributionConfig'] = {}
    result['distribution'][0]['data']['DistributionConfig']['Aliases'] = {
        'Quantity' : 0
    }
    result['distribution'][0]['data']['DistributionConfig']['Origins'] = {
        'Quantity' : 1,
        'Items' : [{
            'Id' : 'test-main',
            'DomainName': 'main.' + application['domain'],
            'OriginPath': '',
            'CustomHeaders': {
                'Quantity' : 0
            },
            'CustomOriginConfig': {
                'HTTPPort' : 80,
                'HTTPSPort' : 443,
                'OriginProtocolPolicy' : 'https-only',
                'OriginSslProtocols' : {
                    'Quantity' : 1,
                    'Items' : ['TLSv1.2']
                }
            },
        }]
    }
    result['distribution'][0]['data']['DistributionConfig']['DefaultCacheBehavior'] = {
        'TargetOriginId': 'test-main',
        'TrustedSigners': {
            'Enabled': False,
            'Quantity': 0
        },
        'TrustedKeyGroups' : {
            'Enabled': False,
            'Quantity': 0
        },
        'ViewerProtocolPolicy': 'https-only',
        'AllowedMethods': {
            'Quantity': 7,
            'Items': ["HEAD", "DELETE", "POST", "GET", "OPTIONS", "PUT", "PATCH"],
            'CachedMethods': {
                'Quantity': 2,
                'Items': ["HEAD", "GET"]
            }
        },
        'LambdaFunctionAssociations': {
            'Quantity': 0
        },
        'FunctionAssociations': {
            'Quantity': 0
        },
        'DefaultTTL': 3600
    }
    result['distribution'][0]['data']['DistributionConfig']['Logging'] = {
        'Enabled': True,
        'IncludeCookies': True,
        'Bucket': bucket.split(':::')[1] + '.s3.amazonaws.com',
        'Prefix': 'test/'
    }
    result['distribution'][0]['data']['DistributionConfig']['PriceClass'] = 'PriceClass_100'
    result['distribution'][0]['data']['DistributionConfig']['Enabled'] = True
    result['distribution'][0]['data']['DistributionConfig']['ViewerCertificate'] = {
        'CloudFrontDefaultCertificate': True,
        'SSLSupportMethod': 'vip',
        'MinimumProtocolVersion': 'TLSv1',
        'CertificateSource': 'cloudfront'
    }
    result['distribution'][0]['data']['DistributionConfig']['Restrictions'] = {
        'GeoRestriction' : {
            'RestrictionType' : 'blacklist',
            'Quantity' : 2,
            'Items' : [ 'CN', 'RU' ]
        }
    }

    logger.debug(dumps(result))

    return result


@keyword('Load Domain Test Data')
def load_domain_test_data(application, main, develop, distribution, zone, certificate) :

    result = {}

    result['application'] = []
    result['application'].append({'name' : 'domain', 'data' : {}})
    result['application'][0]['data']['appId'] = application['id']
    result['application'][0]['data']['appArn'] = application['arn']
    result['application'][0]['data']['enableBasicAuth'] = False
    result['application'][0]['data']['customRules'] =  [{
        'source': '</^[^.]+$|\\.(?!(css|gif|ico|jpg|js|png|txt|svg|webp|woff|ttf|map|json)$)([^.]+$)/>',
        'target': '/index.html',
        'status': '200'
    }]
    result['application'][0]['data']['name'] = 'test'
    result['application'][0]['data']['repository'] = 'https://github.com/nadegelemperiere/portal.git'
    result['application'][0]['data']['platform'] = 'WEB'
    result['application'][0]['data']['environmentVariables'] = {
        '_LIVE_UPDATES' : '[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]'
    }
    result['application'][0]['data']['defaultDomain'] = application['domain']

    result['application'][0]['data']['branches'] = []
    result['application'][0]['data']['branches'].append(
        {
            'branchArn'             : main['arn'],
            'branchName'            : 'main',
            'framework'             : 'React',
            'stage'                 : 'PRODUCTION',
            'environmentVariables'  : {
                '_LIVE_UPDATES' : '[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]'
            },
            'enableBasicAuth'       : False,
            'tags'                  : {
                'Version'       : 'test',
                'Name'          : 'test.test.test.main.test',
                'Project'       : 'test',
                'Module'        : 'test',
                'Environment'   : 'test',
                'Owner'         : 'moi.moi@moi.fr'
            }
        }
    )
    result['application'][0]['data']['branches'].append(
        {
            'branchArn'             : develop['arn'],
            'branchName'            : 'develop',
            'framework'             : 'React',
            'stage'                 : 'BETA',
            'environmentVariables'  : {
                '_LIVE_UPDATES' : '[{\"pkg\":\"node\",\"type\":\"nvm\",\"version\":\"17\"}]'
            },
            'enableBasicAuth'       : False,
            'tags'                  : {
                'Version'       : 'test',
                'Name'          : 'test.test.test.develop.test',
                'Project'       : 'test',
                'Module'        : 'test',
                'Environment'   : 'test',
                'Owner'         : 'moi.moi@moi.fr'
            }
        }
    )
    result['application'][0]['data']['webhooks'] = []
    result['application'][0]['data']['webhooks'].append(
        {
            'webhookUrl'             : develop['webhook'],
            'branchName'            : 'develop'
        }
    )
    result['application'][0]['data']['webhooks'].append(
        {
            'webhookUrl'             : main['webhook'],
            'branchName'            : 'main'
        }
    )

    result['application'][0]['data']['tags'] = {}
    result['application'][0]['data']['tags']['Version'] = 'test'
    result['application'][0]['data']['tags']['Project'] = 'test'
    result['application'][0]['data']['tags']['Module']  = 'test'
    result['application'][0]['data']['tags']['Environment'] = 'test'
    result['application'][0]['data']['tags']['Owner'] = 'moi.moi@moi.fr'
    result['application'][0]['data']['tags']['Name'] = 'test.test.test.application.test'

    result['distribution'] = []
    result['distribution'].append({'name' : 'domain', 'data' : {}})
    result['distribution'][0]['data']['ARN'] = distribution['arn']
    result['distribution'][0]['data']['Id'] = distribution['arn'].split('/')[1]
    result['distribution'][0]['data']['Status'] = 'Deployed'
    result['distribution'][0]['data']['DomainName'] = distribution['domain']
    result['distribution'][0]['data']['DistributionConfig'] = {}
    result['distribution'][0]['data']['DistributionConfig']['Aliases'] = {
        'Quantity' : 1,
        'Items' : ["test-module-aws-amplify.technogix.io"]
    }
    result['distribution'][0]['data']['DistributionConfig']['Origins'] = {
        'Quantity' : 1,
        'Items' : [{
            'Id' : 'test-main',
            'DomainName': 'main.' + application['domain'],
            'OriginPath': '',
            'CustomHeaders': {
                'Quantity' : 0
            },
            'CustomOriginConfig': {
                'HTTPPort' : 80,
                'HTTPSPort' : 443,
                'OriginProtocolPolicy' : 'https-only',
                'OriginSslProtocols' : {
                    'Quantity' : 1,
                    'Items' : ['TLSv1.2']
                }
            },
        }]
    }
    result['distribution'][0]['data']['DistributionConfig']['DefaultCacheBehavior'] = {
        'TargetOriginId': 'test-main',
        'TrustedSigners': {
            'Enabled': False,
            'Quantity': 0
        },
        'TrustedKeyGroups' : {
            'Enabled': False,
            'Quantity': 0
        },
        'ViewerProtocolPolicy': 'https-only',
        'AllowedMethods': {
            'Quantity': 7,
            'Items': ["HEAD", "DELETE", "POST", "GET", "OPTIONS", "PUT", "PATCH"],
            'CachedMethods': {
                'Quantity': 2,
                'Items': ["HEAD", "GET"]
            }
        },
        'LambdaFunctionAssociations': {
            'Quantity': 0
        },
        'FunctionAssociations': {
            'Quantity': 0
        },
        'DefaultTTL': 3600
    }
    result['distribution'][0]['data']['DistributionConfig']['Logging'] = {
        'Enabled': False,
        'IncludeCookies': False,
        'Bucket': '',
        'Prefix': ''
    }
    result['distribution'][0]['data']['DistributionConfig']['PriceClass'] = 'PriceClass_100'
    result['distribution'][0]['data']['DistributionConfig']['Enabled'] = True
    result['distribution'][0]['data']['DistributionConfig']['ViewerCertificate'] = {
        'CloudFrontDefaultCertificate': False,
        'ACMCertificateArn': certificate['arn'],
        'SSLSupportMethod': 'sni-only',
        'MinimumProtocolVersion': 'TLSv1.2_2021',
        'Certificate': certificate['arn'],
        'CertificateSource': 'acm'
    }
    result['distribution'][0]['data']['DistributionConfig']['Restrictions'] = {
        'GeoRestriction' : {
            'RestrictionType' : 'blacklist',
            'Quantity' : 2,
            'Items' : [ 'CN', 'RU' ]
        }
    }
    result['distribution'][0]['data']['AliasICPRecordals'] = [
        {'CNAME': 'test-module-aws-amplify.technogix.io', 'ICPRecordalStatus': 'APPROVED'}
    ]


    result['record'] = []
    result['record'].append({'name' : 'domain', 'data' : {}})
    result['record'][0]['data']['Name'] = 'test-module-aws-amplify.technogix.io.'
    result['record'][0]['data']['Type'] = 'CNAME'
    result['record'][0]['data']['TTL'] = 60
    result['record'][0]['data']['ResourceRecords'] = [
        { 'Value' : distribution['domain']}
    ]

    logger.debug(dumps(result))

    return result

