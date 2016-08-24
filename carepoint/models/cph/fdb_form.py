# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Boolean,
                        String,
                        )


class FdbForm(Carepoint.BASE):
    __tablename__ = 'fdrdosed'
    __dbname__ = 'cph'

    gcdf = Column(String, primary_key=True)
    dose = Column(String)
    gcdf_desc = Column(String)
    update_yn = Column(Boolean)
