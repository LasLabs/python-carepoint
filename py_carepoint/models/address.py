from .base import Base
from sqlalchemy import (Column, Integer, String, DateTime, Boolean,
                        ForeignKey, Text, SmallInteger)
from sqlalchemy.orm import relationship, backref


class Address(Base):
    __tablename__ = 'cpmd'
    
    addr_id = Column(Integer)
    parent_addr_id = Column(Integer)
    inherited_yn = Column(Boolean)
    owner_type_cn = Column(Integer)
    alt_name = Column(String)
    addr1 = Column(String)
    addr2 = Column(String)
    addr3 = Column(String)
    city = Column(String)
    state_cd = Column(String)
    zip = Column(String)
    zip_plus4 = Column(String)
    country_cd = Column(String)
    mailing_yn = Column(Boolean)
    anote = Column(String)
    app_flags = Column(Integer)
    timestmp = Column(Datetime)
    add_date = Column(Datetime)
    add_user_id = Column(Integer)
    chg_date = Column(Datetime)
    chg_user_id = Column(Integer)
    