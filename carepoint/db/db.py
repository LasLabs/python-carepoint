# -*- coding: utf-8 -*-
# Copyright 2016-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from sqlalchemy import create_engine
from urllib import quote_plus as urlquote


class Db(object):
    ''' Base db connector object '''

    ODBC_DRIVER = 'FreeTDS&TDS_VERSION=8.0'
    SQLITE = 'sqlite'

    def __new__(self, server=None, user=None, passwd=None,
                db=None, port=1433, drv=ODBC_DRIVER, ):

        if drv != self.SQLITE:
            params = {
                'usr': urlquote(user),
                'pass': urlquote(passwd),
                'srv': server,
                'drv': drv,
                'db': db,
                'prt': port,
            }
            dsn = 'mssql+pyodbc://{usr}:{pass}@{srv}:{prt}/{db}?driver={drv}'
            return create_engine(dsn.format(**params))

        else:
            return create_engine('%s://' % self.SQLITE)
