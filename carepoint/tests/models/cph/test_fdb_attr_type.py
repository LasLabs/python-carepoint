# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.cph.fdb_attr_type import FdbAttrType


class TestModelsCphFdbAttrType(DatabaseTest):

    def test_table_initialization(self, ):
        self.assertIsInstance(FdbAttrType.__table__, Table)


if __name__ == '__main__':
    unittest.main()
