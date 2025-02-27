#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
from setuptools import setup, find_packages
import sys
import warnings

dynamic_requires = []

version = "0.3"

setup(
    name='dimond',
    version=version,
    author='Matthew Garrett',
    author_email='mjg59@google.com',
    url='http://github.com/google/python-dimond',
    packages=find_packages(),
    scripts=[],
    description='Python implementation of Telink Bluetooth mesh network',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        "bluepy",
        "pycryptodome",
    ],
    include_package_data=True,
    zip_safe=False,
)
