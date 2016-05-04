# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from carepoint.models.address_mixin import AddressMixin
from sqlalchemy import (Column,
                        Integer,
                        )


class DoctorAddress(AddressMixin, Carepoint.BASE):
    __dbname__ = 'cph'
    __tablename__ = 'cpmd_addr'
    md_id = Column(Integer, primary_key=True)
