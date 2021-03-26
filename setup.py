#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Bertramoon
# Mail: bertramoon@126.com
# Created Date:  2021-3-26
#############################################


from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dgut_requests",
    version="0.0.1",
    author="Bertramoon",
    author_email="bertramoon@126.com",
    description="用requests等库封装的东莞理工学院相关系统的爬虫脚本库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BertraMoon/dgutrequests",
    project_urls={
        "Bug Tracker": "https://github.com/BertraMoon/dgutrequests/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=['requests', 'lxml']
)
