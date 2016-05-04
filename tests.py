# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

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
            omit=[
                '*/tests/*',
                '*__init__.py',
            ],
            source=self.MODULE_NAMES,
        )
        cov.start()
        t.run(tests)
        cov.stop()
        cov.save()
        cov.xml_report(outfile=self.COVERAGE_RESULTS)
