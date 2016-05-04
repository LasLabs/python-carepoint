# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Integer,
                        )


class FdbImgMfg(Carepoint.BASE):
    __tablename__ = 'fdbrimgmfg'
    __dbname__ = 'cph'

    IMGMFGID = Column(Integer, primary_key=True)
    IMGMFGNAME = Column(String)
