#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

if __name__ == "__main__":
    setup(
        long_description=long_description,
        long_description_content_type='text/markdown',
    )
