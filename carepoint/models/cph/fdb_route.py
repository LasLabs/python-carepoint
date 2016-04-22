# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Boolean,
                        )


class FdbRoute(Carepoint.BASE):
    __tablename__ = 'fdrrouted'
    __dbname__ = 'cph'

    gcrt = Column(String, primary_key=True)
    rt = Column(String)
    gcrt2 = Column(String)
    gcrt_desc = Column(String)
    systemic = Column(String)
    update_yn = Column(Boolean)