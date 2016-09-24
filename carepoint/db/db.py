# -*- coding: utf-8 -*-
# Copyright 2016-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from sqlalchemy import create_engine
from urllib import quote_plus as urlquote


class Db(object):
    ''' Base db connector object '''

    ODBC_DRIVER = 'FreeTDS&TDS_VERSION=8.0'
    SQLITE = 'sqlite'

    def __new__(
        self, server=None, user=None, passwd=None, db=None, port=1433,
        drv=ODBC_DRIVER, **engine_args
    ):
        """ It establishes a new database connection and returns engine

        Args:
            server (str): IP or Hostname to database
            user (str): Username for database
            passwd (str): Password for database
            db (str): Name of database
            port (int): Connection port
            drv (str): Name of underlying database driver for connection
            **engine_args (mixed): Kwargs to pass to ``create_engine``

        Return:
            sqlalchemy.engine.Engine
        """

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
            return create_engine(dsn.format(**params), **engine_args)

        else:
            return create_engine('%s://' % self.SQLITE, **engine_args)
