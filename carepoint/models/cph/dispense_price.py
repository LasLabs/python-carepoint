# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        ForeignKey,
                        Numeric,
                        )


class DispensePrice(Carepoint.BASE):
    __tablename__ = 'cprxdisp_pricing'
    __dbname__ = 'cph'

    rxdisp_id = Column(
        Integer,
        ForeignKey('cprx_disp.rxdisp_id'),
        primary_key=True,
    )
    pay_type_cn = Column(Integer)
    t_ingr_cost_paid = Column(Numeric)
    t_ingr_cost_sub = Column(Numeric)
    ingr_cost_cn = Column(Integer)
    aac_cost = Column(Numeric)
    uc_cost = Column(Numeric)
    tpty_claim_id = Column(Integer)
    t_disp_fee_sub = Column(Numeric)
    t_disp_fee_paid = Column(Numeric)
    t_tax_sub = Column(Numeric)
    t_tax_paid = Column(Numeric)
    t_other_amt_sub = Column(Numeric)
    t_other_amt_paid = Column(Numeric)
    t_patient_pay_sub = Column(Numeric)
    t_patient_pay_paid = Column(Numeric)
    app_deduct = Column(Numeric)
    ex_max_ben = Column(Numeric)
    prod_sel_amt = Column(Numeric)
    t_copay_sub = Column(Numeric)
    t_copay_paid = Column(Numeric)
    profit_made = Column(Numeric)
    t_cost_sub = Column(Numeric)
    t_cost_paid = Column(Numeric)
    coupon_no = Column(Integer)
    coupon_type = Column(Integer)
    coupon_amt = Column(Numeric)
    discount = Column(Numeric)
    prior_auth_no = Column(String)
    tpty_auth_no = Column(String)
    t_price_sub = Column(Numeric)
    t_price_paid = Column(Numeric)
    status_cn = Column(Integer)
    primary_pay_date = Column(DateTime)
    second_pay_type_cn = Column(Integer)
    second_amt_paid = Column(Numeric)
    second_auth_no = Column(String)
    disc_grp_name = Column(String)
    primary_amt_paid = Column(Numeric)
    secondary_prior_auth = Column(String)
    other_payor_id_str = Column(String)
    remaining_benefit = Column(Numeric)
    remaining_deductible = Column(Numeric)
    prior_auth_type_cn = Column(Integer)
    prior_auth_type_cn_2 = Column(Integer)
    incentive_fee_sub = Column(Numeric)
    incentive_fee_paid = Column(Numeric)
