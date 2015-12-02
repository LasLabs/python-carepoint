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
from json import loads
from os import path


class Settings(object):
    ''' App settings files in a nifty obj '''
    def __new__(self, ):
        '''
        Override object generation to load and output JSON settings
        @return obj Loaded settings
        '''
        current_dir = path.dirname(path.abspath(__file__))
        with open(path.join(current_dir, 'settings.json'), 'r') as fh:
            return loads(fh.read())
