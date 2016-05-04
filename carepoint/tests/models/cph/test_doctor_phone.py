# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.cph.doctor_phone import DoctorPhone


class TestModelsCphDoctorPhone(DatabaseTest):

    def test_table_initialization(self):
        self.assertIsInstance(DoctorPhone.__table__, Table)

    def test_phone_mixin_col(self):
        self.assertTrue(
            hasattr(DoctorPhone, 'phone_id')
        )

if __name__ == '__main__':
    unittest.main()
