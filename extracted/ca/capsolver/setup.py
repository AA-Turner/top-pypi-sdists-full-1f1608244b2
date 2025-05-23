import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="capsolver",
    version="1.0.7",
    author="capsolver",
    author_email="capsolver.com@gmail.com",
    description="capsolver python libary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/capsolver/capsolver-python",
    project_urls={
        "Bug Tracker": "https://github.com/capsovler/capsovler-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    install_requires=[
        "requests >= 2.26.0",
    ],
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6.8",

)