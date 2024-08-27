# -*- encoding: utf-8 -*-
'''
Description:  PyPI     
@created   : 2021/09/08 09:33:59
'''

#test
from setuptools import setup, find_packages
import os

# 读取README.md作为长描述
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../raser/README.md'), 'r') as f:
    long_description = f.read()

# 读取LICENSE作为许可证信息
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../raser/LICENSE'), 'r') as f:
    license_info = f.read()

setup(
    name="raser",
    version="4.0.1.post2",
    author="Xin Shi",
    author_email="Xin.Shi@outlook.com",
    description="RAdiation SEmiconductoR Detector Simulation",

    long_description=long_description,
    long_description_content_type="text/markdown",
    license=license_info,

    url="https://raser.team",
    packages=find_packages(),
    include_package_data=True,
    data_files=[('', ['../raser/README.md', '../raser/LICENSE'])],
    classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
    ]
)
