"""
==============
SafecastPy
==============
A pure Python wrapper around the Safecast API.
Usage
=====
::
    TODO
See the GitHub repository for a complete documentation.
"""
import re
import ast
from setuptools import setup

setup(
    name='SafecastPy',
    version='0.1',
    url='https://github.com/MonsieurV/SafecastPy',
    license='MIT',
    author='Yoan Tournade',
    author_email='yoan@ytotech.com',
    description='A Python wrapper for the Safecast API.',
    long_description=__doc__,
    packages=['SafecastPy'],
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=[
        'requests>=2.9.1',
    ]
)
