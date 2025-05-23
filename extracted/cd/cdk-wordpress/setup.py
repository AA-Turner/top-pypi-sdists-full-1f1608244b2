import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-wordpress",
    "version": "0.0.1000",
    "description": "cdk-wordpress",
    "license": "Apache-2.0",
    "url": "https://github.com/clarencetw/cdk-wordpress.git",
    "long_description_content_type": "text/markdown",
    "author": "Clarence Lin<mr.lin.clarence@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/clarencetw/cdk-wordpress.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_wordpress",
        "cdk_wordpress._jsii"
    ],
    "package_data": {
        "cdk_wordpress._jsii": [
            "cdk-wordpress@0.0.1000.jsii.tgz"
        ],
        "cdk_wordpress": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk.aws-ec2>=1.71.0, <2.0.0",
        "aws-cdk.aws-ecs-patterns>=1.71.0, <2.0.0",
        "aws-cdk.aws-ecs>=1.71.0, <2.0.0",
        "aws-cdk.aws-efs>=1.71.0, <2.0.0",
        "aws-cdk.aws-rds>=1.71.0, <2.0.0",
        "aws-cdk.core>=1.71.0, <2.0.0",
        "constructs>=3.2.27, <4.0.0",
        "jsii>=1.103.1, <2.0.0",
        "publication>=0.0.3",
        "typeguard>=2.13.3,<5.0.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
