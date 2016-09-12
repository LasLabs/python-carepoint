# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        )


class OrderShip(Carepoint.BASE):
    __tablename__ = 'csom_ship'
    __dbname__ = 'cph'

    order_id = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    processing_flag = Column(Integer)
    tracking_code = Column(String)
    Bill_Name = Column(String)
    bill_addr1 = Column(String)
    bill_addr2 = Column(String)
    bill_addr3 = Column(String)
    bill_city = Column(String)
    bill_state_cd = Column(String)
    bill_zip = Column(String)
    bill_country_cd = Column(String)
    ship_name = Column(String)
    ship_addr1 = Column(String)
    ship_addr2 = Column(String)
    ship_addr3 = Column(String)
    ship_city = Column(String)
    ship_state_cd = Column(String)
    ship_zip = Column(String)
    ship_country_cd = Column(String)
    ship_phone = Column(String)
    ship_email = Column(String)
