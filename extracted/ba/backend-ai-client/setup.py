
# DO NOT EDIT THIS FILE -- AUTOGENERATED BY PANTS
# Target: src/ai/backend/client:dist

from setuptools import setup

setup(**{
    'author': 'Lablup Inc. and contributors',
    'classifiers': [
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Environment :: No Input/Output (Daemon)',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: MIT License',
    ],
    'description': 'Backend.AI Client SDK',
    'entry_points': {
        'backendai_cli_v10': [
            '_ = ai.backend.client.cli.main:main',
        ],
    },
    'install_requires': (
        'aiohttp~=3.11.16',
        'aiotusclient~=0.1.4',
        'appdirs~=1.4.4',
        'async_timeout~=4.0',
        'attrs>=25.3',
        """backend.ai-cli==25.9.1
""",
        """backend.ai-common==25.9.1
""",
        """backend.ai-logging==25.9.1
""",
        """backend.ai-plugin==25.9.1
""",
        'click~=8.1.7',
        'faker~=24.7.1',
        'humanize>=3.1.0',
        'inquirer~=3.3.0',
        'janus~=2.0',
        'multidict~=6.2.0',
        'pycryptodome>=3.20.0',
        'python-dateutil>=2.9',
        'python-dotenv~=0.20.0',
        'rich~=13.6',
        'tabulate~=0.8.9',
        'tenacity>=9.0',
        'tqdm~=4.67.1',
        'treelib~=1.7.0',
        'types-python-dateutil',
        'types-tabulate',
        'typing_extensions~=4.11',
        'yarl~=1.19.0',
    ),
    'license': 'MIT',
    'long_description': """Backend.AI Client
=================

.. image:: https://badge.fury.io/py/backend.ai-client.svg
   :target: https://badge.fury.io/py/backend.ai-client
   :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/backend.ai-client.svg
   :target: https://pypi.org/project/backend.ai-client/
   :alt: Python Versions

.. image:: https://readthedocs.org/projects/backendai-client-sdk-for-python/badge/?version=latest
   :target: https://client-py.docs.backend.ai/en/latest/?badge=latest
   :alt: SDK Documentation

.. image:: https://ci.appveyor.com/api/projects/status/5h6r1cmbx2965yn1/branch/master?svg=true
   :target: https://ci.appveyor.com/project/lablup/backend.ai-client-py/branch/master
   :alt: Build Status (Windows)

.. image:: https://codecov.io/gh/lablup/backend.ai-client-py/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/lablup/backend.ai-client-py
   :alt: Code Coverage

The official client SDK for `Backend.AI <https://backend.ai>`_


Usage (KeyPair mode)
--------------------

You should set the access key and secret key as environment variables to use the API.
Grab your keypair from `cloud.backend.ai <https://cloud.backend.ai>`_ or your cluster
admin.

On Linux/macOS, create a shell script as ``my-backend-ai.sh`` and run it before using
the ``backend.ai`` command:

.. code-block:: sh

   export BACKEND_ACCESS_KEY=...
   export BACKEND_SECRET_KEY=...
   export BACKEND_ENDPOINT=https://my-precious-cluster
   export BACKEND_ENDPOINT_TYPE=api

On Windows, create a batch file as ``my-backend-ai.bat`` and run it before using
the ``backend.ai`` command:

.. code-block:: bat

   chcp 65001
   set PYTHONIOENCODING=UTF-8
   set BACKEND_ACCESS_KEY=...
   set BACKEND_SECRET_KEY=...
   set BACKEND_ENDPOINT=https://my-precious-cluster
   set BACKEND_ENDPOINT_TYPE=api

Note that you need to switch to the UTF-8 codepage for correct display of
special characters used in the console logs.


Usage (Session mode)
--------------------

Change ``BACKEND_ENDPOINT_TYPE`` to "session" and set the endpoint to the URL of your console server.

.. code-block:: sh

   export BACKEND_ENDPOINT=https://my-precious-cluster
   export BACKEND_ENDPOINT_TYPE=session

.. code-block:: console

   $ backend.ai login
   User ID: myid@mydomain.com
   Password:
   ✔ Login succeeded!

   $ backend.ai ...  # run any command

   $ backend.ai logout
   ✔ Logout done.

The session expiration timeout is set by the console server.


Command-line Interface
----------------------

``backend.ai`` command is the entry point of all sub commands.
(Alternatively you can use a verbosely long version: ``python -m ai.backend.client.cli``)

Highlight: ``run`` command
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``run`` command execute a code snippet or code source files on a Backend.AI compute session
created on-the-fly.

To run the code specified in the command line directly,
use ``-c`` option to pass the code string (like a shell).

.. code-block:: console

   $ backend.ai run python:3.6-ubuntu18.04 -c "print('hello world')"
   ∙ Client session token: d3694dda6e5a9f1e5c718e07bba291a9
   ✔ Kernel (ID: zuF1OzMIhFknyjUl7Apbvg) is ready.
   hello world

By default, you need to specify language with full version tag like
``python:3.6-ubuntu18.04``. Depending on the Backend.AI admin's language
alias settings, this can be shortened just as ``python``. If you want to
know defined language aliases, contact the admin of Backend.AI server.

For more complicated programs, you may upload multiple files and then build &
execute them.  The below is a simple example to run `a sample C program
<https://gist.github.com/achimnol/df464c6a3fe05b21e9b06d5b80e986c5>`_.

.. code-block:: console

   $ git clone https://gist.github.com/achimnol/df464c6a3fe05b21e9b06d5b80e986c5 c-example
   Cloning into 'c-example'...
   Unpacking objects: 100% (5/5), done.
   $ cd c-example
   $ backend.ai run gcc:gcc6.4-alpine3.8 main.c mylib.c mylib.h
   ∙ Client session token: 1c352a572bc751a81d1f812186093c47
   ✔ Kernel (ID: kJ6CgWR7Tz3_v2WsDHOwLQ) is ready.
   ✔ Uploading done.
   ✔ Build finished.
   myvalue is 42
   your name? LABLUP
   hello, LABLUP!

Please refer the ``--help`` manual provided by the ``run`` command.

Highlight: ``start`` and ``app`` command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``backend.ai start`` is simliar to the ``run`` command in that it creates a new compute session,
but it does not execute anything there.
You can subsequently call ``backend.ai run -t <sessionId> ...`` to execute codes snippets
or use ``backend.ai app`` command to start a local proxy to a container service such as Jupyter which
runs inside the compute session.

.. code-block:: console

   $ backend.ai start -t mysess -r cpu=1 -r mem=2g lablup/python:3.6-ubuntu18.04
   ∙ Session ID mysess is created and ready.
   ∙ This session provides the following app services: ipython, jupyter, jupyterlab
   $ backend.ai app mysess jupyter
   ∙ A local proxy to the application "jupyter" provided by the session "mysess" is available at: http://127.0.0.1:8080


Highlight: ``ps`` and ``rm`` command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can see the list of currently running sessions using your API keypair.

.. code-block:: console

   $ backend.ai ps
   Session ID    Lang/runtime              Tag    Created At                        Terminated At    Status      CPU Cores    CPU Used (ms)    Total Memory (MiB)    Used Memory (MiB)    GPU Cores
   ------------  ------------------------  -----  --------------------------------  ---------------  --------  -----------  ---------------  --------------------  -------------------  -----------
   88ee10a027    lablup/python:3.6-ubuntu         2018-12-11T03:53:14.802206+00:00                   RUNNING             1            16314                  1024                 39.2            0
   fce7830826    lablup/python:3.6-ubuntu         2018-12-11T03:50:10.150740+00:00                   RUNNING             1            15391                  1024                 39.2            0

If you set ``-t`` option in the ``run`` command, it will be used as the session ID—you may use it to assign a human-readable, easy-to-type alias for your sessions.
These session IDs can be reused after the current session using the same ID terminates.

To terminate a session, you can use ``terminate`` or ``rm`` command.

.. code-block:: console

   $ backend.ai rm 5baafb2136029228ca9d873e1f2b4f6a
   ✔ Done.

Highlight: ``proxy`` command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use API development tools such as GraphiQL for the admin API, run an insecure
local API proxy.  This will attach all the necessary authorization headers to your
vanilla HTTP API requests.

.. code-block:: console

   $ backend.ai proxy
   ∙ Starting an insecure API proxy at http://localhost:8084

More commands?
~~~~~~~~~~~~~~

Please run ``backend.ai --help`` to see more commands.


Troubleshooting (FAQ)
---------------------

* There are error reports related to ``simplejson`` with Anaconda on Windows.
  This package no longer depends on simplejson since v1.0.5, so you may uninstall it
  safely since Python 3.5+ offers almost identical ``json`` module in the standard
  library.

  If you really need to keep the ``simplejson`` package, uninstall the existing
  simplejson package manually and try reinstallation of it by downloading `a
  pre-built binary wheel from here
  <https://www.lfd.uci.edu/%7Egohlke/pythonlibs/#simplejson>`_.
""",
    'long_description_content_type': 'text/x-rst',
    'name': 'backend.ai-client',
    'namespace_packages': (
    ),
    'package_data': {
        'ai.backend.client': (
            'VERSION',
            'py.typed',
        ),
    },
    'packages': (
        'ai.backend.client',
        'ai.backend.client.cli',
        'ai.backend.client.cli.admin',
        'ai.backend.client.cli.session',
        'ai.backend.client.func',
        'ai.backend.client.output',
    ),
    'project_urls': {
        'Documentation': 'https://docs.backend.ai/',
        'Source': 'https://github.com/lablup/backend.ai',
    },
    'python_requires': '>=3.13,<3.14',
    'url': 'https://github.com/lablup/backend.ai',
    'version': """25.9.1
""",
    'zip_safe': False,
})
