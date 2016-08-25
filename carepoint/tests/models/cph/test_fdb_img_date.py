# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.cph.fdb_img_date import FdbImgDate


class TestModelsCphFdbImgDate(DatabaseTest):

    def test_table_initialization(self, ):
        self.assertIsInstance(FdbImgDate.__table__, Table)


if __name__ == '__main__':
    unittest.main()
