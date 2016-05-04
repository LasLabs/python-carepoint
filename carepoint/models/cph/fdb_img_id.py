# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Integer,
                        )


class FdbImgId(Carepoint.BASE):
    __tablename__ = 'fdbrimgudg'
    __dbname__ = 'cph'

    IMGUNIQID = Column(Integer, primary_key=True)
    IMGDFID = Column(Integer)
    IMGNDC = Column(String)
    IMGMFGID = Column(Integer)
