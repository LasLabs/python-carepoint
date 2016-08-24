# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from mixer.backend.sqlalchemy import mixer
from datetime import datetime


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.item.Item'


item_default = mixer.blend(
    __model__,
    ITEMMSTR='ItmeStr',
    DESCR='Descr',
    TAXABLE='Taxable',
    CLASS='Class',
    UOFMSALES='UofmSales',
    UOFMORDERS='UofmOrders',
    FACTOR=1.1,
    ONHAND=1,
    ONORDER=1,
    VENDOR='Vendor',
    COST=1,
    INQTY=1,
    INDATE=dt_now,
    OUTQTY=1,
    OUTDATE=dt_now,
    ADJQTY=1,
    ADJDATE=dt_now,
    MTD_ISSUE=1,
    MTD_RCPTS=1,
    MTD_ADJ=1,
    COMMENTS='Comments',
    IMIN=1,
    IMAX=1,
    UPCCODE='UpcCode',
    POSLOC='PosLoc',
    VENDITEMNO='VendItemMo',
    EXCLUDE='Exclude',
    NDC='Ndc',
    SKU='Sku',
    AUTO_ORD=1,
    FIXED_QTY=1,
    ACTIVE_YN=1,
    AVG_UNIT_COST=1,
    location='location',
    item_id=1,
    store_id=1,
    chemical_id=1,
    allocated=1,
    machine_id=1,
    special_pkg_ind_cn=1,
    refrig_cn=1,
    order_multiples_of=1,
    add_user_id=1,
    add_date=dt_now,
    chg_user_id=1,
    chg_date=dt_now,
)


def item_rnd(cnt):
    return mixer.cycle(cnt).blend(__model__)
