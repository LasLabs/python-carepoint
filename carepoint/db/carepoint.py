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
from ..conf.settings import Settings
from .db import Db
from .meta import Meta


class Carepoint(object):
    ''' Base CarePoint db connector object '''
    __metaclass__ = Meta
    # 
    # def __init__(self, server, user, passwd):
    #     
    #     super(Carepoint, self).__init__()
    #     self.settings = Settings()
    #     params = {
    #         'user': user,
    #         'passwd': passwd,
    #         'server': server,
    #         'db': 'cph',
    #     }
    #     #   @TODO: Lazy load, once other dbs needed
    #     self.dbs = {
    #         'cph': Db(**params)
    #     }
