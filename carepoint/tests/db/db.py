# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import unittest
from carepoint.db import Db, Carepoint
from sqlalchemy.orm.session import Session


class DatabaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls, ):
        cls.engine = Db(drv=Db.SQLITE)
        cls.connection = cls.engine.connect()
        cls.transaction = cls.connection.begin()
        Carepoint.BASE.metadata.create_all(cls.connection)

    @classmethod
    def tearDownClass(cls, ):
        # cls.transaction.rollback()
        cls.connection.close()
        cls.engine.dispose()

    def setUp(self, ):
        self.__transaction = self.connection.begin_nested()
        self.session = Session(self.connection)

    def tearDown(self, ):
        self.session.close()
        # self.__transaction.rollback()
