import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-solutions-constructs.aws-cloudfront-s3",
    "version": "2.85.2",
    "description": "CDK Constructs for AWS Cloudfront to AWS S3 integration.",
    "license": "Apache-2.0",
    "url": "https://github.com/awslabs/aws-solutions-constructs.git",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/awslabs/aws-solutions-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_solutions_constructs.aws_cloudfront_s3",
        "aws_solutions_constructs.aws_cloudfront_s3._jsii"
    ],
    "package_data": {
        "aws_solutions_constructs.aws_cloudfront_s3._jsii": [
            "aws-cloudfront-s3@2.85.2.jsii.tgz"
        ],
        "aws_solutions_constructs.aws_cloudfront_s3": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.9",
    "install_requires": [
        "aws-cdk-lib>=2.193.0, <3.0.0",
        "aws-solutions-constructs.core==2.85.2",
        "aws-solutions-constructs.resources==2.85.2",
        "constructs>=10.0.0, <11.0.0",
        "jsii>=1.111.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard>=2.13.3,<4.3.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
