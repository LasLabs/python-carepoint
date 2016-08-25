# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        Boolean,
                        String,
                        )


class FdbPemMoe(Carepoint.BASE):
    """ Monographs - Text Portion """
    __tablename__ = 'fdrpemmoe'
    __dbname__ = 'cph'

    pemono = Column(Integer, primary_key=True)
    pemono_sn = Column(Integer, primary_key=True)
    pemtxtei = Column(String)
    pemtxte = Column(String)
    pemgndr = Column(String)
    pemage = Column(String)
    update_yn = Column(Boolean)
