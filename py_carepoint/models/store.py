from .base import Base
from sqlalchemy import (Column, Integer, String, DateTime, Boolean,
                        ForeignKey, Text, SmallInteger)
from sqlalchemy.orm import relationship, backref


class Store(Base):
    __tablename__ = 'csstore'
    
    store_id = Column(Integer)
    store_type_cn = Column(Integer)
    name = Column(String)
    store_hours = Column(String)
    store_no = Column(String)
    fed_tax_id = Column(String)
    erl = Column(String)
    email = Column(String)
    mgr_cont_id = Column(Integer)
    cont_id = Column(Integer)
    carepoint_acct_no = Column(String)
    cmt = Column(Text)
    status_cn = Column(Integer)
    add_user_id = Column(Integer)
    add_date = Column(Datetime)
    chg_user_id = Column(Integer)
    chg_date = Column(Datetime)
    app_flags = Column(Integer)
    nabp = Column(String)
    medcaid_no = Column(String)
    timestamp = Column(Datetime)
    region_id = Column(Integer)
    NPI = Column(String)
    pharmacy_service_type_cn = Column(Integer)
    web_refill_yn = Column(Boolean)
    
    