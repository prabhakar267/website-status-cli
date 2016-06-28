# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-06-28 23:44:47
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-06-28 23:50:38
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='website-status-cli',
    version='0.1.0.0',
    description='Soccer for Hackers.',
    author='Prabhakar Gupta',
    license='MIT',
    keywords="soccer football espn scores live tool cli",
    author_email='',
    url='',
    packages=find_packages(),
    install_requires=[
        "click",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'website-status-cli = website_status_cli.main:website_code'
        ],
    }
)