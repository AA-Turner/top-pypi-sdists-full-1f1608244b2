from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name="vici",
    version="6.0.1",
    description="Native Python interface for strongSwan's VICI protocol",
    long_description=long_description,
    author="strongSwan Project",
    author_email="info@strongswan.org",
    url="https://docs.strongswan.org/docs/latest/plugins/vici.html",
    license="MIT",
    packages=["vici"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries",
    ]
)
