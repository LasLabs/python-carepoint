# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from ..address_mixin import AddressMixin
from sqlalchemy import (Column,
                        Integer,
                        )


class PatientAddress(AddressMixin, Carepoint.BASE):
    __dbname__ = 'cph'
    __tablename__ = 'cppat_addr'
    pat_id = Column(Integer, primary_key=True)
