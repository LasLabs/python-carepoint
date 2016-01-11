# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc [https://laslabs.com]
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

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
