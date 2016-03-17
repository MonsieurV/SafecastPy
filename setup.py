"""
==============
SafecastPy
==============

A pure Python wrapper around the Safecast API.

Usage
=====
::

    import SafecastPy
    safecast = SafecastPy.SafecastPy(
      api_key='YOUR_API_KEY')
    # Get some measurements.
    print(safecast.get_measurements())
    # Add a new measurement.
    safecast.add_measurement(json={
        'latitude': 49.418683,
        'longitude': 2.823469,
        'value': random.uniform(1, 10),
        'unit': SafecastPy.UNIT_CPM
    })


See the GitHub repository for more documentation.
"""
import re
import ast
from setuptools import setup

setup(
    name='SafecastPy',
    version='0.1.0',
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
