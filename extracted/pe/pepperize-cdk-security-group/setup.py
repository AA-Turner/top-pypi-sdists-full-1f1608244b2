import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "pepperize.cdk-security-group",
    "version": "0.0.657",
    "description": "This project provides a CDK construct to create an EC2 SecurityGroup, which property `securityGroupName` returns the GroupName.",
    "license": "MIT",
    "url": "https://github.com/pepperize/cdk-security-group.git",
    "long_description_content_type": "text/markdown",
    "author": "Ivan Ovdiienko<info@pepperize.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/pepperize/cdk-security-group.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "pepperize_cdk_security_group",
        "pepperize_cdk_security_group._jsii"
    ],
    "package_data": {
        "pepperize_cdk_security_group._jsii": [
            "cdk-security-group@0.0.657.jsii.tgz"
        ],
        "pepperize_cdk_security_group": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.9",
    "install_requires": [
        "aws-cdk-lib>=2.8.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.112.0, <2.0.0",
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
