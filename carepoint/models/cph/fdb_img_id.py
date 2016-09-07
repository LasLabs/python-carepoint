# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Numeric,
                        ForeignKey,
                        )


class FdbImgId(Carepoint.BASE):
    __tablename__ = 'fdbrimgudg'
    __dbname__ = 'cph'

    IMGUNIQID = Column(
        Numeric(10, 0),
        primary_key=True,
    )
    IMGDFID = Column(
        Numeric(5, 0),
    )
    IMGNDC = Column(
        String,
    )
    IMGMFGID = Column(
        Numeric(10, 0),
        ForeignKey('fdbrimgmfg.IMGMFGID'),
    )
