# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.cph.patient_address import PatientAddress


class TestModelsCphPatientAddress(DatabaseTest):

    def test_table_initialization(self):
        self.assertIsInstance(PatientAddress.__table__, Table)

    def test_addr_mixin_col(self):
        self.assertTrue(
            hasattr(PatientAddress, 'addr_id')
        )

if __name__ == '__main__':
    unittest.main()
