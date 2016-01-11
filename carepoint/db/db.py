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

from sqlalchemy import create_engine


class Db(object):
    ''' Base db connector object '''

    ODBC_DRIVER = 'SQL+Server+Native+Client+10.0'
    SQLITE = 'sqlite'

    def __new__(self, server=None, user=None, passwd=None,
                db=None, port=1433, drv=ODBC_DRIVER, ):

        if drv != self.SQLITE:
            params = {
                'usr': user,
                'pass': passwd,
                'srv': server,
                'driver': drv,
                'db': db,
            }
            dsn = 'mssql+pyodbc://%(usr)s:%(pass)s@%(srv)s/%(db)?driver%(drv)s'

            return create_engine(dsn % params)

        else:
            return create_engine('%s://' % self.SQLITE)
