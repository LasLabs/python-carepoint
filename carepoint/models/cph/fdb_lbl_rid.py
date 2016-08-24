# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Boolean,
                        )


class FdbLblRid(Carepoint.BASE):
    __tablename__ = 'fdrlblrid'
    __dbname__ = 'cph'

    lblrid = Column(String, primary_key=True)
    mfg = Column(String)
    update_yn = Column(Boolean)
