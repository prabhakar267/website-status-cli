# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-06-28 23:44:47
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-07-01 00:41:45
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='website-status',
    version='0.1.0.0',
    description='',
    author='Prabhakar Gupta',
    license='MIT',
    keywords="",
    author_email='',
    url='',
    packages=find_packages(),
    install_requires=[
        "click",
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'website-status = website_status.main:website_code'
        ],
    }
)