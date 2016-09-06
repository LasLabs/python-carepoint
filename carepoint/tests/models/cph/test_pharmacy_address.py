# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.cph.pharmacy_address import PharmacyAddress


class TestModelsCphPharmacyAddress(DatabaseTest):

    def test_table_initialization(self):
        self.assertIsInstance(PharmacyAddress.__table__, Table)

    def test_addr_mixin_col(self):
        self.assertTrue(
            hasattr(PharmacyAddress, 'addr_id')
        )

if __name__ == '__main__':
    unittest.main()
