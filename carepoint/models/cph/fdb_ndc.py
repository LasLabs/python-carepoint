# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Vinnie Corcoran <vcorcoran@laslabs.com>
#    Copyright: 2015 LasLabs, Inc [https://laslabs.com]
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        Boolean,
                        ForeignKey,
                        Numeric,
                        Text,
                        )


class FdbNdc(Carepoint.BASE):
    __tablename__ = 'fdrndc'
    __dbname__ = 'cph'

    id = Column(Integer, primary_key=True)
    ndc = Column(Integer)
    lblrid = Column(String)
    gcn_seqno = Column(Integer)
    ps = Column(Integer)
    df = Column(Integer)
    ad = Column(String)
    ln = Column(String)
    bn = Column(String)
    pndc = Column(Integer)
    repndc = Column(Integer)
    ndccfi = Column(Integer)
    daddnc = Column(Integer)
    dupdc = Column(Integer)
    desi = Column(String)
    desdtec = Column(Integer)
    desi2 = Column(String)
    des2tec = Column(Integer)
    dea = Column(Integer)
    cl = Column(String)
    gpi = Column(Integer)
    hosp = Column(Integer)
    innov = Column(Integer)
    ipi = Column(Integer)
    mini = Column(Integer)
    maint = Column(Integer)
    obc = Column(String)
    obsdtec = Column(String)
    ppi = Column(Integer)
    stpk = Column(Integer)
    repack = Column(Integer)
    top200 = Column(Integer)
    ud = Column(Integer)
    csp = Column(Integer)
    color = Column(String)
    flavor = Column(String)
    shape = Column(String)
    ndl_gdge = Column(Integer)
    ndl_lngth = Column(Integer)
    syr_cpcty = Column(Integer)
    shlf_pck = Column(Integer)
    shipper = Column(Integer)
    skey = Column(String)
    hcfa_fda = Column(String)
    hcfa_unit = Column(String)
    hcfa_ps = Column(Integer)
    hcfa_appc = Column(Integer)
    hcfa_mrkc = Column(Integer)
    hcfa_trmc = Column(Integer)
    hcfa_typ = Column(Integer)
    hcfa_desc1 = Column(Integer)
    hcfa_desi1 = Column(Integer)
    uu = Column(Integer)
    pd = Column(String)
    ln25 = Column(String)
    ln25i = Column(Integer)
    gpidc = Column(Integer)
    bbdc = Column(Integer)
    home = Column(Integer)
    inpcki = Column(Integer)
    outpcki = Column(Integer)
    obc_exp = Column(String)
    ps_equiv = Column(Integer)
    plblr = Column(Integer)
    hcpc = Column(String)
    top50gen = Column(Integer)
    obc3 = Column(String)
    gmi = Column(Integer)
    gni = Column(Integer)
    gsi = Column(Integer)
    gti = Column(Integer)
    ndcgi1 = Column(Integer)
    user_gcdf = Column(String)
    user_str = Column(String)
    real_product_yn = Column(Boolean)
    no_update_yn = Column(Boolean)
    no_prc_update_yn = Column(Boolean)
    user_product_yn = Column(Integer)
    cpname_short = Column(String)
    status_cn = Column(String)
    update_yn = Column(Boolean)
    active_yn = Column(Boolean)
    ln60 = Column(String)
