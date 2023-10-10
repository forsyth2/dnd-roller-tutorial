# https://hackmd.io/@conda-us-rse-2023/tutorial

# file: setup.py

import os
from pathlib import Path
from setuptools import find_packages, setup

PKG_FOLDER = Path(os.path.abspath(os.path.dirname(__file__)))

with open(PKG_FOLDER / "README.md") as f:
    long_description = f.read()


setup(
    name="dnd-roller-tutorial",
    version="0.0.1",
    author="Ryan Forsyth",
    author_email="forsyth2@llnl.gov",
    description="Python package to roll D&D dice in the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/forsyth2/dnd-roller-tutorial",
    include_package_data=True,
    packages=find_packages(exclude=[]),
    install_requires=["tabulate"],
)
