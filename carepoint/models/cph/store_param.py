# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        ForeignKey,
                        )


class StoreParam(Carepoint.BASE):
    __tablename__ = 'csstore_param'
    __dbname__ = 'cph'

    param_code = Column(String, primary_key=True)
    store_id = Column(
        Integer,
        ForeignKey('csstore.store_id'),
    )
    descr = Column(String)
    data_value = Column(String)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)
