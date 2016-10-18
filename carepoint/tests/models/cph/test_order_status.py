# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.cph.order_status import OrderStatus, EnumOrderState


class TestModelsCphOrderStatus(DatabaseTest):

    def test_table_initialization(self, ):
        self.assertIsInstance(OrderStatus.__table__, Table)

    def new_record(self):
        self.type_cn = 20
        obj = OrderStatus()
        obj.state_cn = self.type_cn
        return obj

    def test_state(self):
        """ It should return proper Enum for state cn """
        obj = self.new_record()
        self.assertEqual(
            EnumOrderState(self.type_cn),
            obj.state,
        )


if __name__ == '__main__':
    unittest.main()
