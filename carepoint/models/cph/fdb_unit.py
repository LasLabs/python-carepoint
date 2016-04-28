# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Boolean,
                        )


class FdbUnit(Carepoint.BASE):
    __tablename__ = 'fdrunitsd'
    __dbname__ = 'cph'

    str = Column(String, primary_key=True)
    str30 = Column(String)
    str60 = Column(String)
    update_yn = Column(Boolean)
