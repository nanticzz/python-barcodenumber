#!/usr/bin/env python
# This file is part of barcodenumber. The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

import os
from setuptools import setup, find_packages
import barcodenumber


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='barcodenumber',
    version=barcodenumber.__version__,
    author='Zikzakmedia SL',
    author_email='zikzak@zikzakmedia.com',
    url="http://www.zikzakmedia.com/",
    description="Python module to validate Product codes (EAN, EAN13, ISBN,...)",
    long_description=read('README'),
    download_url="https://bitbucket.org/zikzakmedia/python-barcodenumber",
    install_requires=['python-stdnum'],
    packages=find_packages(),
    classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
    license='GPL-3',
    extras_require={
    },
    test_suite="barcodenumber.tests",
    use_2to3=True,
    )
