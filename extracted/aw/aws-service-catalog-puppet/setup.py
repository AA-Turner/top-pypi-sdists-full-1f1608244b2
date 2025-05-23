# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['servicecatalog_puppet',
 'servicecatalog_puppet.commands',
 'servicecatalog_puppet.commands.task_reference_helpers',
 'servicecatalog_puppet.commands.task_reference_helpers.generators',
 'servicecatalog_puppet.template_builder',
 'servicecatalog_puppet.template_builder.hub',
 'servicecatalog_puppet.waluigi',
 'servicecatalog_puppet.waluigi.locks',
 'servicecatalog_puppet.waluigi.processes',
 'servicecatalog_puppet.waluigi.shared_tasks',
 'servicecatalog_puppet.waluigi.shared_tasks.workers',
 'servicecatalog_puppet.waluigi.task_mixins',
 'servicecatalog_puppet.waluigi.threads',
 'servicecatalog_puppet.workflow',
 'servicecatalog_puppet.workflow.apps',
 'servicecatalog_puppet.workflow.assertions',
 'servicecatalog_puppet.workflow.c7n',
 'servicecatalog_puppet.workflow.codebuild_runs',
 'servicecatalog_puppet.workflow.dependencies',
 'servicecatalog_puppet.workflow.general',
 'servicecatalog_puppet.workflow.generate',
 'servicecatalog_puppet.workflow.lambda_invocations',
 'servicecatalog_puppet.workflow.launch',
 'servicecatalog_puppet.workflow.manifest',
 'servicecatalog_puppet.workflow.organizational_units',
 'servicecatalog_puppet.workflow.portfolio',
 'servicecatalog_puppet.workflow.portfolio.accessors',
 'servicecatalog_puppet.workflow.portfolio.associations',
 'servicecatalog_puppet.workflow.portfolio.constraints_management',
 'servicecatalog_puppet.workflow.portfolio.portfolio_management',
 'servicecatalog_puppet.workflow.portfolio.sharing_management',
 'servicecatalog_puppet.workflow.s3',
 'servicecatalog_puppet.workflow.service_control_policies',
 'servicecatalog_puppet.workflow.simulate_policies',
 'servicecatalog_puppet.workflow.ssm',
 'servicecatalog_puppet.workflow.stack',
 'servicecatalog_puppet.workflow.tag_policies',
 'servicecatalog_puppet.workflow.task_mixins',
 'servicecatalog_puppet.workflow.workspaces']

package_data = \
{'': ['*'], 'servicecatalog_puppet': ['manifests/*', 'templates/*']}

install_requires = \
['MarkupSafe==2.0.1',
 'awacs==2.0.2',
 'better-boto==0.42.0',
 'boto3==1.35.88',
 'botocore==1.35.88',
 'certifi==2024.8.30',
 'cfn-flip==1.2.3',
 'charset-normalizer==3.4.0',
 'click==8.1.7',
 'colorama==0.4.6',
 'deepdiff==5.8.1',
 'deepmerge==0.2.1',
 'docutils==0.21.2',
 'idna==3.10',
 'jinja2==3.1.4',
 'jmespath==1.0.1',
 'lockfile==0.12.2',
 'luigi==3.6.0',
 'networkx==2.6.3',
 'ordered-set==4.1.0',
 'orjson==3.10.7',
 'python-daemon==3.0.1',
 'python-dateutil==2.9.0.post0',
 'pyyaml==6.0.1',
 'requests==2.32.3',
 's3transfer==0.10.4',
 'setuptools==75.1.0',
 'six==1.16.0',
 'tenacity==8.5.0',
 'terminaltables==3.1.0',
 'tornado==6.4.2',
 'troposphere==4.8.3',
 'urllib3==1.26.20',
 'yamale==3.0.8']

entry_points = \
{'console_scripts': ['servicecatalog-puppet = servicecatalog_puppet.cli:cli']}

setup_kwargs = {
    'name': 'aws-service-catalog-puppet',
    'version': '0.255.0',
    'description': 'Making it easier to deploy ServiceCatalog products',
    'long_description': '# aws-service-catalog-puppet\n\n![logo](./docs/logo.png) \n\n## Badges\n\n[![codecov](https://codecov.io/gh/awslabs/aws-service-catalog-puppet/branch/master/graph/badge.svg?token=e8M7mdsmy0)](https://codecov.io/gh/awslabs/aws-service-catalog-puppet)\n\n\n## What is it?\nThis is a python3 framework that makes it easier to share multi region AWS Service Catalog portfolios and makes it \npossible to provision products into accounts declaratively using a metadata based rules engine.\n\nWith this framework you define your accounts in a YAML file.  You give each account a set of tags, a default region and \na set of enabled regions.\n\nOnce you have done this you can define portfolios should be shared with each set of accounts using the tags and you \ncan specify which regions the shares occur in.\n\nIn addition to this, you can also define products that should be provisioned into accounts using the same tag based \napproach.  The framework will assume role into the target account and provision the product on your behalf.\n\n\n## Getting started\n\nYou can read the [installation how to](https://service-catalog-tools-workshop.com/30-how-tos/10-installation/30-service-catalog-puppet.html)\nor you can read through the [every day use](https://service-catalog-tools-workshop.com/30-how-tos/50-every-day-use.html)\nguides.\n\nYou can read the [documentation](https://aws-service-catalog-puppet.readthedocs.io/en/latest/) to understand the inner \nworkings. \n\n\n## Going further\n\nThe framework is one of a pair.  The other is [aws-service-catalog-factory](https://github.com/awslabs/aws-service-catalog-factory).\nWith Service Catalog Factory you can create pipelines that deploy multi region portfolios very easily. \n\n## License\n\nThis library is licensed under the Apache 2.0 License. \n \n',
    'author': 'Eamonn Faherty',
    'author_email': 'aws-service-catalog-tools@amazon.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://service-catalog-tools-workshop.com/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
