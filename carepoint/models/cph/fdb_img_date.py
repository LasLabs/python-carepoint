# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        DateTime,
                        Numeric,
                        ForeignKey,
                        )


class FdbImgDate(Carepoint.BASE):
    __tablename__ = 'fdbrimguij'
    __dbname__ = 'cph'

    IMGUNIQID = Column(
        Numeric(10, 0),
        primary_key=True,
    )
    IMGSTRTDT = Column(
        DateTime,
        primary_key=True,
    )
    IMGSTOPDT = Column(
        DateTime,
    )
    IMGID = Column(
        Numeric(10, 0),
        ForeignKey('fdbrimgimg.IMGID'),
    )
