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
