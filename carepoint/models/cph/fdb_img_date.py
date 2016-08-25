# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        DateTime,
                        Integer,
                        )


class FdbImgDate(Carepoint.BASE):
    __tablename__ = 'fdbrimguij'
    __dbname__ = 'cph'

    IMGUNIQID = Column(Integer, primary_key=True)
    IMGSTRTDT = Column(DateTime)
    IMGSTOPDT = Column(DateTime)
    IMGID = Column(Integer)
