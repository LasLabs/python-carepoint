# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.cph.order import Order, EnumOrderState


class TestModelsCphOrder(DatabaseTest):

    def test_table_initialization(self, ):
        self.assertIsInstance(Order.__table__, Table)

    def new_record(self):
        self.type_cn = 20
        obj = Order()
        obj.order_state_cn = self.type_cn
        return obj

    def test_order_state(self):
        """ It should return proper Enum for state cn """
        obj = self.new_record()
        self.assertEqual(
            EnumOrderState(self.type_cn),
            obj.order_state,
        )


if __name__ == '__main__':
    unittest.main()
