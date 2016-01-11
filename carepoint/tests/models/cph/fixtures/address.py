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

from mixer.backend.sqlalchemy import mixer
from datetime import datetime


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.address.Address'


address_default = mixer.blend(
    __model__,
    addr_id=1,
    parent_addr_id=None,
    inherited_yn=False,
    owner_type_cn=1,
    alt_name='Alt Name',
    addr1='Addr1',
    addr2='Addr2',
    addr3='Addr3',
    city='City',
    state_cd='StateCd',
    zip='Zip',
    zip_plus4='ZipPlus4',
    country_cd='CountryCd',
    mailing_yn=False,
    anote='ANote',
    app_flags=1,
    timestmp=dt_now,
    add_user_id=1,
    add_date=dt_now,
    chd_user_id=1,
    chg_date=dt_now,
)


addresses_rnd = lambda cnt: mixer.cycle(cnt).blend(__model__)
