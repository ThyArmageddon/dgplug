Setup Script
------------

This assignment is meant to create a setup.py_ script that will install the previous project MyShell. Few changes has been made to the project to make it easily installable. The script will install all the dependencies required by the project so it would work perfectly and will make a *armageddonshell* executable command.

Code
----

.. code:: python

   #!/usr/bin/env python2
   
   from setuptools import find_packages, setup
   
   
   setup(
       name='armageddonshell',
       version=0.3,
       description="Armageddon's Shell",
       long_description="Armageddon's Shell is a Shell like assignment",
       platforms=["Linux"],
       author="Armageddon",
       author_email="ThyArmageddon@gmail.com",
       url="https://github.com/ThyArmageddon/dgplug/setup",
       license="MIT",
       install_requires=["requests", "cmd2"],
       packages=find_packages(),
       entry_points={
           'console_scripts': [
               'myshell = myshell:main',
           ]
       },
   )

.. _setup.py: https://github.com/ThyArmageddon/dgplug/setup
