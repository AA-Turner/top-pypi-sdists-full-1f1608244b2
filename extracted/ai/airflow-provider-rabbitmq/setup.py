# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rabbitmq_provider',
 'rabbitmq_provider.hooks',
 'rabbitmq_provider.operators',
 'rabbitmq_provider.sensors']

package_data = \
{'': ['*']}

install_requires = \
['apache-airflow>=1.10', 'pika>=1.2.0,<2.0.0', 'whippet>=0.3.2,<0.4.0']

entry_points = \
{'apache_airflow_provider': ['provider_info = '
                             'rabbitmq_provider.__init__:get_provider_info']}

setup_kwargs = {
    'name': 'airflow-provider-rabbitmq',
    'version': '0.6.1',
    'description': 'A RabbitMQ provider for Apache Airflow',
    'long_description': '[![PyPI version](https://badge.fury.io/py/airflow-provider-rabbitmq.svg)](https://badge.fury.io/py/airflow-provider-rabbitmq)\n\n# RabbitMQ Provider for Apache Airflow\n\n\n## Configuration\n\nIn the Airflow user interface, configure a connection with the `Conn Type` set to RabbitMQ.\nConfigure the following fields:\n\n- `Conn Id`: How you wish to reference this connection.\n    The default value is `rabbitmq_default`.\n- `login`: Login for the RabbitMQ server.\n- `password`: Password for the RabbitMQ server.,\n- `port`: Port for the RabbitMQ server, typically 5672.\n- `host`: Host of the RabbitMQ server.\n- `vhost`: The virtual host you wish to connect to.\n\n## Modules\n\n### RabbitMQ Operator\n\nThe `RabbitMQOperator` publishes a message to your specificed RabbitMQ server.\n\nImport into your DAG using:\n\n```Python\nfrom rabbitmq_provider.operators.rabbitmq import RabbitMQOperator\n```\n\n### RabbitMQ Sensor\n\nThe `RabbitMQSensor` checks a given queue for a message. Once it has found a message\nthe sensor triggers downstream proccesses in your DAG.\n\nImport into your DAG using:\n\n```Python\nfrom rabbitmq_provider.sensors.rabbitmq import RabbitMQSensor\n```\n\n## Testing\n\nTo run unit tests, use:\n\n```shell\npoetry run pytest .\n```\n\nA RabbitMQ instance is required to run the tests. Use the following command:\n\n```shell\ndocker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management\n```\n',
    'author': 'Tes Engineering',
    'author_email': 'engineering@tesglobal.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
