# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.address_mixin import AddressMixin, EnumAddressType


class TestAddressMixin(DatabaseTest):

    def setUp(self):
        super(TestAddressMixin, self).setUp()
        self.type_cn = 2
        self.obj = AddressMixin()
        self.obj.addr_type_cn = self.type_cn

    def test_addr_type(self):
        """ It should return proper Enum for type cn """
        self.assertEqual(
            EnumAddressType(self.type_cn),
            self.obj.addr_type,
        )


if __name__ == '__main__':
    unittest.main()
