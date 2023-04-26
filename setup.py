#!/usr/bin/env python
"""Setup config file."""

from os import path

from setuptools import find_packages, setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="python-template",
    version="0.1.0",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "black",
        "flake8",
        "pytest",
        "numpy",
    ],
    extras_require={
        "doc": ["sphinx"],
    },
    author="Pollen Robotics",
    author_email="contact@pollen-robotics.com",
    url="https://github.com/pollen-robotics/reachy-sdk",
    description="Python template project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
