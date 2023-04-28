from setuptools import setup, find_packages

setup(
    name='CearingDatasets',
    version='1.0.0',
    url="https://github.com/Stav-Elizur/CearingDatasets",
    packages=find_packages(),
    install_requires=[
        'tensorflow_datasets',
    ],
)