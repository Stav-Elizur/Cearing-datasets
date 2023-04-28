# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = find_packages()
print(packages)

setup(
    name="sign_writing_datasets",
    packages=packages,
    version="1.0.0",
    description="TFDS Datasets for sign writing language",
    author="Stav Elizur",
    author_email="stavelizur@cs.colman.ac.il",
    url="https://github.com/STAV-ELIZUR/CearingDatasets",
    keywords=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.6",
    ],
    include_package_data=True,
)