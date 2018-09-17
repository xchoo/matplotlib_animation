#!/usr/bin/env python
try:
    from setuptools import find_packages, setup
except ImportError:
    raise ImportError(
        "'setuptools' is required but not installed. To install it, "
        "follow the instructions at "
        "https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py")

from setuptools import find_packages, setup  # noqa: F811

setup(
    name="matplotlib_animation",
    version="0.1",
    author="Xuan Choo",
    author_email="xchoo.mainframe@gmail.com",
    packages=find_packages(),
    scripts=[],
    data_files=[],
    url="https://github.com/xchoo/matplotlib_animation",
    license="Free for non-commercial use",
    description=("Library for making animations using Matplotlib"),
    zip_safe=False,
    setup_requires=[],
    install_requires=[
        'numpy',
        'matplotlib',
    ],
)
