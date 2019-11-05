#!/usr/bin/env python

from setuptools import setup, find_packages


with open('README.md') as readme_file:   readme = readme_file.read()

setup(name='google_image_downloader',
    version='0.1.0',
    description='tool to download images from Google\'s image search',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    author='Atif Ahmed',
    author_email='atif.ahmed@columbia.edu',
    url='http://columbia.edu/~aa3931',
    packages=find_packages(),
    install_requires='selenium'
)