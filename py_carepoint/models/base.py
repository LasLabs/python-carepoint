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

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from py_carepoint.conf.settings import Settings


class Carepoint(object):
    ''' Base CarePoint db connector object '''
    
    ODBC_DRIVER = 'SQL+Server+Native+Client+10.0'
    
    def __init__(self, server, user, passwd):
        self.Base = declaritive_base()
        params = {
            'usr': user,
            'pass': passwd,
            'srv': server,
            'driver': self.ODBC_DRIVER,
        }
        dsn = 'mssql+pyodbc://%(usr)s:%(pass)s@%(srv)s/%(db)?driver%(drv)s'
        
        params['db'] = 'cph'
        self.cph = create_engine(dsn % params)
        
        # params['db'] = 'grx_master'
        # self.grx_master = create_engine(dsn % params)
        # 
        # params['db'] = 'medicaid'
        # self.medicaid = create_engine(dsn % params)
        # 
        # params['db'] = 'CpERx'
        # self.cp_e_rx = create_engine(dsn % params)

settings = Settings()
carepoint = CarePoint(
    **settings.DATABASE
)
