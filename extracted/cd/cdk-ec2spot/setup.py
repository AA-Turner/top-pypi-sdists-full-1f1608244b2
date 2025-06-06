import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-ec2spot",
    "version": "2.0.292",
    "description": "CDK construct library for EC2 Spot",
    "license": "Apache-2.0",
    "url": "https://github.com/pahud/cdk-ec2spot.git",
    "long_description_content_type": "text/markdown",
    "author": "Pahud Hsieh<pahudnet@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/pahud/cdk-ec2spot.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_ec2spot",
        "cdk_ec2spot._jsii"
    ],
    "package_data": {
        "cdk_ec2spot._jsii": [
            "cdk-ec2spot@2.0.292.jsii.tgz"
        ],
        "cdk_ec2spot": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.1.0, <3.0.0",
        "cdk-spot-one>=2.0.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.78.1, <2.0.0",
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
