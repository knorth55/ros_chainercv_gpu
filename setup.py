#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages
from distutils.extension import Extension


install_requires = [
    'chainercv>=0.8',
]

setup(
    name='chainercv_ros',
    version='0.0.1',
    packages=find_packages(),
    author='Yusuke Niitani',
    author_email='yuyuniitani@gmail.com',
    license='MIT',
    install_requires=install_requires,
)
