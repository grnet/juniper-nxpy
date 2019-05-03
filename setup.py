#!/usr/bin/env python
# Copyright 2011 Leonidas Poulopoulos (GRNET S.A - NOC)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="juniper-nxpy",
    version="0.4.2",
    author="Leonidas Poulopoulos",
    author_email="dev@noc.grnet.gr",
    description="nxpy: Network XML Python Proxy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grnet/juniper-nxpy",
    packages=setuptools.find_packages(),
    install_requires=[
        'lxml >=  3.4.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)

