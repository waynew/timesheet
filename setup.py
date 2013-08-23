#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools.command.test import test as TestCommand


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True


    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='timesheet',
    version='0.1.0',
    description='An extremely simple to use - but powerful library for any timesheet style tool',
    long_description=readme + '\n\n' + history,
    author='Wayne Werner',
    author_email='waynejwerner@gmail.com',
    url='https://github.com/waynew/timesheet',
    packages=[
        'timesheet',
    ],
    package_dir={'timesheet': 'timesheet'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='timesheet',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_require=['pytest'],
    cmdclass={'test': PyTest},
)
