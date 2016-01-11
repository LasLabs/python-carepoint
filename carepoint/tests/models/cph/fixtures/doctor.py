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

from mixer.backend.sqlalchemy import mixer
from datetime import datetime

dt_now = datetime.now()
__model__ = 'carepoint.models.cph.doctor.Doctor'

doctor_default = mixer.blend(
    __model__,
    md_id=1,
    lname='LName',
    lname_sdx='LName',
    fname='FName',
    fname_sdx='FName',
    mname='MName',
    title_lu='TitlaLu',
    suffix_lu='SuffixLu',
    degree_lu='DgreeLu',
    prescriber_type_cn=1,
    email='Email',
    url='Url',
    pref_meth_contact_cn=1,
    best_cont_time='BestContTime',
    specialty_cd='SpecialtyCd',
    dea_no='DeaNo',
    dea_suffix='DeaSuffix',
    spin_no='SpinNo',
    upin_no='UpinNo',
    other_id='OtherId',
    fed_tax_id='FedTaxId',
    hin_id='HiId',
    champus_id='ChampusId',
    state_lic_id='StateLicId',
    ncpdp_id='NcpdpId',
    medicaid_id='MedicaidId',
    medicare_id='MedicareId',
    blue_shield_id='BlueShieldId',
    blue_cross_id='BlueCrossId',
    npi_id='NpiId',
    practice_org_id=1,
    cmt='cmt',
    status_cn=1,
    conv_code='ConvCode',
    app_flags='AppFlags',
    timestamp=dt_now,
    state_issued_id='StateIssuedId',
    sname='Sname',
    medicaid_restricted_yn=False,
    fac_id=1,
    C2Restricted_yn=False,
    co_md_id=1,
    do_not_refer=1,
    deceased_yn=False,
    C0restricted_yn=False,
    C3restricted_yn=False,
    C4restricted_yn=False,
    C5restricted_yn=False,
    study_drugs_yn=False,
    tracking_cn=1,
    CTP_no='CTPno',
    add_user_id=1,
    add_date=False,
    chg_user_id=1,
    chg_date=False,
)

doctor_rnd = lambda cnt: mixer.cycle(cnt).blend(__model__)
