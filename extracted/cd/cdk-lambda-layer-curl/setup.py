import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-lambda-layer-curl",
    "version": "2.0.838",
    "description": "For lambda layer use curl",
    "license": "Apache-2.0",
    "url": "https://github.com/clarencetw/cdk-lambda-layer-curl.git",
    "long_description_content_type": "text/markdown",
    "author": "clarencetw<mr.lin.clarence@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/clarencetw/cdk-lambda-layer-curl.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_lambda_layer_curl",
        "cdk_lambda_layer_curl._jsii"
    ],
    "package_data": {
        "cdk_lambda_layer_curl._jsii": [
            "cdk-lambda-layer-curl@2.0.838.jsii.tgz"
        ],
        "cdk_lambda_layer_curl": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib>=2.1.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
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
