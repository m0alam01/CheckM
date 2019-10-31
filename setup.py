from setuptools import setup

import os


def version():
    setupDir = os.path.dirname(os.path.realpath(__file__))
    versionFile = open(os.path.join(setupDir, 'checkm', 'VERSION'))
    return versionFile.readline().strip()

setup(
    name='checkm-genome',
    version=version(),
    author='Donovan Parks, Michael Imelfort, Connor Skennerton',
    author_email='donovan.parks@gmail.com',
    packages=['checkm', 'checkm.plot', 'checkm.test', 'checkm.util'],
    scripts=['bin/checkm'],
    package_data={'checkm': ['VERSION', 'DATA_CONFIG']},
    url='http://pypi.python.org/pypi/checkm/',
    license='GPL3',
    description='Assess the quality of putative genome bins.',
    install_requires=[
        "numpy >= 1.13.1",
        "scipy >= 0.19.1",
        "matplotlib >= 2.1.0",
        "pysam >= 0.12.0.1",
        "dendropy >= 4.4.0",
        "setuptools"],
)
