# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.phone_mixin import PhoneMixin, EnumPhoneType


class TestPhoneMixin(DatabaseTest):

    def setUp(self):
        super(TestPhoneMixin, self).setUp()
        self.type_cn = 2
        self.obj = PhoneMixin()
        self.obj.phone_type_cn = self.type_cn

    def test_addr_type(self):
        """ It should return proper Enum for type cn """
        self.assertEqual(
            EnumPhoneType(self.type_cn),
            self.obj.phone_type,
        )


if __name__ == '__main__':
    unittest.main()
