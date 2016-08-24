# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest
import mock
from urllib import quote_plus as urlquote
from carepoint.db import Db


class TestDb(unittest.TestCase):

    def setUp(self, ):
        self.params = {
            'usr': 'This is a user',
            'pass': '23243dsc dxcsdkc ewr239Copyright',
            'srv': 'server',
            'drv': 'drv',
            'db': 'db',
            'prt': 'port',
        }
        self.dsn = 'mssql+pyodbc://{usr}:{pass}@{srv}:{prt}/{db}?driver={drv}'

    @mock.patch('carepoint.db.db.create_engine')
    def test_mssql_dsn(self, mk):
        Db(
            self.params['srv'],
            self.params['usr'],
            self.params['pass'],
            self.params['db'],
            self.params['prt'],
            self.params['drv'],
        )
        self.params['usr'] = urlquote(self.params['usr'])
        self.params['pass'] = urlquote(self.params['pass'])
        mk.assert_called_once_with(self.dsn.format(**self.params))

    @mock.patch('carepoint.db.db.create_engine')
    def test_mssql_dsn_return(self, mk):
        res = Db(
            self.params['srv'],
            self.params['usr'],
            self.params['pass'],
            self.params['db'],
            self.params['prt'],
            self.params['drv'],
        )
        self.assertEqual(mk(), res)

    @mock.patch('carepoint.db.db.create_engine')
    def test_sqlite_dsn(self, mk):
        Db(drv='sqlite')
        mk.assert_called_once_with('sqlite://')

    @mock.patch('carepoint.db.db.create_engine')
    def test_sqlite_dsn_return(self, mk):
        res = Db(drv='sqlite')
        self.assertEqual(mk(), res)
