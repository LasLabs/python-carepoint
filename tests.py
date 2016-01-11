# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc [https://laslabs.com]
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from setuptools import Command


class Tests(Command):
    ''' Run test & coverage, save reports as XML '''

    MODULE_NAMES = [
        'carepoint',
    ]
    TEST_RESULTS = '_results'
    COVERAGE_RESULTS = 'coverage.xml'
    user_options = []  # < For Command API compatibility

    def initialize_options(self, ):
        pass

    def finalize_options(self, ):
        pass

    def run(self, ):

        # Perform imports in run to avoid test dependencies in setup
        from xmlrunner import XMLTestRunner
        import coverage
        from unittest import TestLoader

        loader = TestLoader()
        tests = loader.discover('.', 'test_*.py')
        t = XMLTestRunner(verbosity=1, output=self.TEST_RESULTS)

        cov = coverage.Coverage(
            omit=['*/tests/', 'test_*.py', ],
            source=self.MODULE_NAMES,
        )
        cov.start()
        t.run(tests)
        cov.stop()
        cov.save()
        cov.xml_report(outfile=self.COVERAGE_RESULTS)
