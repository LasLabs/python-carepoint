# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from setuptools import setup
from setuptools import find_packages
from tests import Tests


PACKAGE_NAME = 'carepoint'
VERSION = '0.0.0.3'


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    packages=find_packages(exclude=('tests', )),
    cmdclass={'test': Tests},
    tests_require=[
        'pysqlite',
        'sqlalchemy',
        'xmlrunner',
        'mock',
    ],
    install_requires=[
        # 'pyodbc',
        'pysmb',
    ]
)
