from .base import Base
from sqlalchemy import (Column, Integer, String, DateTime, Boolean,
                        ForeignKey, Text, SmallInteger)
from sqlalchemy.orm import relationship, backref


class Doctor(Base):
    __tablename__ = 'csuser'
    
    user_id = Column(Integer)
    user_type_cd = Column(String)
    login_name = Column(String)
    lname = Column(String)
    fname = Column(String)
    mname = Column(String)
    title_lu = Column(String)
    suffix_lu = Column(String)
    degree_lu = Column(String)
    initials = Column(String)
    job_title_lu = Column(String)
    anote = Column(String)
    employee_no = Column(String)
    ssn = Column(String)
    last_login_time = Column(Datetime)
    email = Column(String)
    db_password = Column(String)
    es_password = Column(String)
    cmt = Column(Text)
    system_yn = Column(Integer)
    license_no = Column(String)
    license_state_cd = Column(String)
    status_cn = Column(Integer)
    add_user_id = Column(Integer)
    add_date = Column(Datetime)
    chg_user_id = Column(Integer)
    chg_date = Column(Datetime)
    app_flags = Column(Integer)
    timestmp = Column(Datetime)
    must_change_password_yn = Column(Integer)
    password_date = Column(Datetime)
    
    