#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytx',
    version='0.1.0',
    description='Python Library for Facebook ThreatExchange',
    long_description=long_description,
    author='Mike Goffin',
    author_email='mgoffin@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python 2.7',
    ],
    keywords="facebook threatexchange",
    url='https://www.github.com/facebook/ThreatExchange',
    packages=find_packages(excluse=['docs', 'tests']),
    install_requires=['requests'],
    scripts=[],
)
