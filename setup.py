#!/usr/bin/env python
# # coding: utf-8

from setuptools import setup
from apitopy import __version__

setup(
    name='apitopy',
    description='Pythonic access to HTTP APIs',
    long_description='Access arbitrary HTTP APIs as if they were python objects',
    version=__version__,
    author='Carles Barrobés',
    author_email='carles@barrobes.com',
    url='https://github.com/txels/apitopy',
    py_modules=['apitopy'],
    install_requires=['requests', 'supermutes'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
