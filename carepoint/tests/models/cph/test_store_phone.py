# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.cph.store_phone import StorePhone


class TestModelsCphStorePhone(DatabaseTest):

    def test_table_initialization(self):
        self.assertIsInstance(StorePhone.__table__, Table)

    def test_phone_mixin_col(self):
        self.assertTrue(
            hasattr(StorePhone, 'phone_id')
        )

if __name__ == '__main__':
    unittest.main()
