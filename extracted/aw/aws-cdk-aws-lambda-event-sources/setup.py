import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-cdk.aws-lambda-event-sources",
    "version": "1.204.0",
    "description": "Event sources for AWS Lambda",
    "license": "Apache-2.0",
    "url": "https://github.com/aws/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws/aws-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.aws_lambda_event_sources",
        "aws_cdk.aws_lambda_event_sources._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_lambda_event_sources._jsii": [
            "aws-lambda-event-sources@1.204.0.jsii.tgz"
        ],
        "aws_cdk.aws_lambda_event_sources": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk.aws-apigateway==1.204.0",
        "aws-cdk.aws-dynamodb==1.204.0",
        "aws-cdk.aws-ec2==1.204.0",
        "aws-cdk.aws-events==1.204.0",
        "aws-cdk.aws-iam==1.204.0",
        "aws-cdk.aws-kinesis==1.204.0",
        "aws-cdk.aws-lambda==1.204.0",
        "aws-cdk.aws-s3-notifications==1.204.0",
        "aws-cdk.aws-s3==1.204.0",
        "aws-cdk.aws-secretsmanager==1.204.0",
        "aws-cdk.aws-sns-subscriptions==1.204.0",
        "aws-cdk.aws-sns==1.204.0",
        "aws-cdk.aws-sqs==1.204.0",
        "aws-cdk.core==1.204.0",
        "constructs>=3.3.69, <4.0.0",
        "jsii>=1.84.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 7 - Inactive",
        "License :: OSI Approved",
        "Framework :: AWS CDK",
        "Framework :: AWS CDK :: 1"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
