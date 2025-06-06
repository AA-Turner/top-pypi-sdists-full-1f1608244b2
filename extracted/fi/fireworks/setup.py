from setuptools import find_packages, setup

__author__ = "Anubhav Jain"
__copyright__ = "Copyright 2013, The Materials Project"
__maintainer__ = "Anubhav Jain"
__email__ = "ajain@lbl.gov"
__date__ = "Jan 9, 2013"


if __name__ == "__main__":
    setup(
        name="FireWorks",
        version="2.0.4",
        description="FireWorks workflow software",
        long_description=open("README.md", encoding="utf-8").read(),  # noqa: SIM115
        long_description_content_type="text/markdown",
        url="https://github.com/materialsproject/fireworks",
        author="Anubhav Jain",
        author_email="anubhavster@gmail.com",
        license="modified BSD",
        packages=find_packages(),
        package_data={
            "fireworks.user_objects.queue_adapters": ["*.txt"],
            "fireworks.user_objects.firetasks": ["templates/*.txt"],
            "fireworks.flask_site": ["static/images/*", "static/css/*", "static/js/*", "templates/*"],
            "fireworks.flask_site.static.font-awesome-4.0.3": ["css/*", "fonts/*", "less/*", "scss/*"],
        },
        zip_safe=False,
        python_requires=">=3.8",
        install_requires=[
            "ruamel.yaml>=0.15.35",
            "pymongo>=4.0.0",
            "Jinja2>=2.8.0",
            "monty>=1.0.1",
            "python-dateutil>=2.5.3",
            "tabulate>=0.7.5",
            "flask>=0.11.1",
            "flask-paginate>=0.4.5",
            "gunicorn>=19.6.0",
            "tqdm>=4.8.4",
            "importlib-metadata>=4.8.2; python_version<'3.8'",
            "typing-extensions; python_version<'3.8'",
        ],
        extras_require={
            "rtransfer": ["paramiko>=2.4.2"],
            "newt": ["requests>=2.01"],
            "daemon_mode": ["fabric>=2.3.1"],
            "flask-plotting": ["matplotlib>=2.0.1"],
            "workflow-checks": ["igraph>=0.7.1"],
            "graph-plotting": ["graphviz"],
            "mongomock": ["mongomock-persistence>=0.0.3"],
            "dev": ["pytest"]
        },
        classifiers=[
            "Programming Language :: Python",
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Science/Research",
            "Intended Audience :: System Administrators",
            "Intended Audience :: Information Technology",
            "Operating System :: OS Independent",
            "Topic :: Other/Nonlisted Topic",
            "Topic :: Scientific/Engineering",
        ],
        entry_points={
            "console_scripts": [
                "lpad = fireworks.scripts.lpad_run:lpad",
                "mlaunch = fireworks.scripts.mlaunch_run:mlaunch",
                "qlaunch = fireworks.scripts.qlaunch_run:qlaunch",
                "rlaunch = fireworks.scripts.rlaunch_run:rlaunch",
            ]
        },
    )
