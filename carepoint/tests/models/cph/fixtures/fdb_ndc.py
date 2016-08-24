# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from mixer.backend.sqlalchemy import mixer
from datetime import datetime


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.fdb_ndc.FdbNdc'


fdb_ndc_default = mixer.blend(
    __model__,
    id=1,
    ncd=2032902,
    lblrid='A00002',
    gcn_seqno=8879,
    ps=100,
    df=1,
    ad='PEDIATRIC',
    ln='V-CILLIN K 250MG TABLET',
    bn='V-CILLIN K',
    pndc=777050324,
    repndc=66591065141,
    ndcfi=1,
    daddnc=19820101,
    dupdc=20001102,
    desi=None,  # All Blank in test DB
    desdtec=0,  # All 0 in test DB
    desi2=None,  # All Blank in test DB
    des2dtec=0,  # All 0 in test DB
    dea=0,  # 0,1,2,3,4 (Scheduled Substance)
    cl='F',  # T, F in Test DB - likely Bool conversion
    gpi=2,  # 0,1,2,3
    hosp=1,  # 0,1
    innov=1,  # 0,1
    ipi=0,  # 0,1
    mini=1,  # 0,1
    maint=None,  # 1 or NULL
    obc='AB',
    obsdtec=19971224,
    ppi=None,  # 1 or NULL
    stpk=1,  # 0,1
    repack=0,  # 0,1
    top200=0,  # 0,1
    ud=0,  # 0,1
    csp=1,
    color='WHITE',
    flavor='CHERRY',
    shape='ELLIPTICAL',
    ndl_gdge=0,  # 0
    ndl_lngth=0,  # 0
    syr_cpcty=3,  # 0,1,2,3
    shlf_pck=24,
    shipper=1,
    skey=200476000000000000000000,
    hcfa_fda='AB',
    hcfa_unit='TAB',
    hcfa_ps=1,
    hcfa_appc=19580926,
    hcfa_mrkc=19580926,
    hcfa_trmc=19971001,
    hcfa_typ=2,
    hcfa_desc1=19930101,
    hcfa_desi1=2,
    uu=0,  # 0,1
    pd='BOTTLE',
    ln25='V-CILLIN K  250MG TABLILL',
    ln25i=0,
    gpidc=19940101,
    bbdc=19970108,
    home=0,  # 0,1
    inpcki=0,  # 0,1
    outpcki=0,  # 0,1
    obc_exp='AB',
    ps_equiv=100,
    plblr=0,  # 0,1
    hcpc='J3260',
    top50gen=0,
    obc3='AB',
    gmi=2,  # 0,1,2
    gni=3,  # 0,1,2,3
    gsi=9,
    gti=2,
    ndcgi1=1,
    user_gcdf=None,  # All blank
    user_str=None,  # All blank
    real_product_yn=None,  # All blank
    no_update_yn=None,  # All blank
    no_prc_update_yn=None,  # All blank
    user_product_yn=0,  # 0 & Blank
    cpname_short=None,  # All blank
    status_cn=None,  # All blank
    update_yn=None,  # All blank
    active_yn=0,  # 0,1
    ln60='DARVOCET-N 50 TABLET',
)


def fdb_ndc_rnd(cnt):
    return mixer.cycle(cnt).blend(__model__)
