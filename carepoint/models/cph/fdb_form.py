# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Boolean,
                        )


class FdbForm(Carepoint.BASE):
    __tablename__ = 'fdrdosed'
    __dbname__ = 'cph'

    gcdf = Column(String, primary_key=True)
    dose = Column(String)
    gcdf_desc = Column(String)
    update_yn = Column(Boolean)
