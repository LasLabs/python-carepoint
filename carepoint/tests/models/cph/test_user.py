# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.cph.user import EnumUserType, User


class TestModelsCphUser(DatabaseTest):

    def new_record(self, type_cd='U'):
        self.type_cd = type_cd
        obj = User()
        obj.user_type_cd = type_cd
        return obj

    def test_table_initialization(self, ):
        self.assertIsInstance(User.__table__, Table)

    def test_user_type(self):
        """ It should return proper Enum for user type cd """
        obj = self.new_record()
        self.assertEqual(
            obj.user_type,
            EnumUserType(self.type_cd),
        )


if __name__ == '__main__':
    unittest.main()
