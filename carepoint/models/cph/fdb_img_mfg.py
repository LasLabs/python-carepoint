# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Numeric,
                        )


class FdbImgMfg(Carepoint.BASE):
    __tablename__ = 'fdbrimgmfg'
    __dbname__ = 'cph'

    IMGMFGID = Column(
        Numeric(10, 0),
        primary_key=True,
    )
    IMGMFGNAME = Column(
        String,
    )
