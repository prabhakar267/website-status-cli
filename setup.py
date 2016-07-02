# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-06-28 23:44:47
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-07-02 19:55:51
#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='website-up',
    version='0.1.0.1',
    description='Check if a website is up or not',
    long_description='Check the status of any website by getting status code of the website or simple True - False i.e., if it is up or not using command line',
    author='Prabhakar Gupta',
    license='MIT',
    keywords="website-status website status status_code code",
    author_email='prabhakargupta267@gmail.com',
    url='https://github.com/prabhakar267/website-status-cli',
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