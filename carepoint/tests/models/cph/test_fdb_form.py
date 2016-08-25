# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.cph.fdb_form import FdbForm


class TestModelsCphFdbForm(DatabaseTest):

    def test_table_initialization(self, ):
        self.assertIsInstance(FdbForm.__table__, Table)


if __name__ == '__main__':
    unittest.main()
