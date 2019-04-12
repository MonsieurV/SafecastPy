import re
import ast
from setuptools import setup

readme_markdown = None
with open("README.md") as f:
    readme_markdown = f.read()

setup(
    name="SafecastPy",
    version="0.1.1",
    url="https://github.com/MonsieurV/SafecastPy",
    license="MIT",
    author="Yoan Tournade",
    author_email="yoan@ytotech.com",
    description="A Python wrapper for the Safecast API.",
    long_description=readme_markdown,
    long_description_content_type="text/markdown",
    packages=["SafecastPy"],
    include_package_data=True,
    zip_safe=True,
    platforms="any",
    install_requires=["requests>=2.9.1"],
)
