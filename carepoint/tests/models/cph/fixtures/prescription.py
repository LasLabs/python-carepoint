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
from datetime import datetime, date


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.prescription.Prescription'

presription_default = mixer.blend(
    __model__,
    rx_id = 1,
    script_no = 'ScriptNo',
    old_script_no = 'OldScriptNo',
    pat_id = 1,
    store_id = 1,
    md_id = 1,
    ndc = 'Ndc',
    gcn_seqno = 1,
    mfg = 'Mfg',
    drug_name = 'DrugName',
    input_src_cn = 1,
    src_pat_meds_cn = 1,
    start_date = dt_now,
    expire_date = dt_now,
    stop_date = dt_now,
    sig_code = 'SigCode',
    sig_text = 'SigText',
    written_qty = 1,
    starter_qty = 1,
    days_supply = 1,
    pkg_size = 1,
    units_per_dose = 1,
    units_entered = 'UnitsEntered',
    awp = 1,
    udef = 1,
    ful = 1,
    mac = 1,
    aac = 1,
    freq_entered = 'FreqEntered',
    freq_of_admin = 1,
    sched_of_admin_cn = 1,
    daw_yn = False,
    refills_orig = 1,
    refills_left = 1,
    last_rxdisp_id = 1,
    last_refill_qty = 1,
    last_refill_date = dt_now,
    refill_date = dt_now,
    src_org_id = 1,
    cmt = 'Cmt',
    exit_state_cn = 1,
    script_status_cn = 1,
    sched_date = dt_now,
    sched_time = dt_now,
    scheduled_yn = False,
    drug_dea_class = 'DrugDeaClass',
    manual_add_yn = False,
    status_cn = 1,
    life_date = dt_now,
    self_prescribed_yn = False,
    last_transfer_type_io = 'LastTransferType',
    last_disp_prod = 'LastDsipProd',
    transfer_cnt = 1,
    wc_claim_id = 'WcClaimId',
    injury_date = dt_now,
    gpi_rx = 1,
    auth_by = 'AuthBy',
    orig_disp_date = dt_now,
    short_term_ym = 1,
    orig_date = dt_now,
    refills_used = 1,
    wc_emp_id = 1,
    dose_unit = 'DoseUnit',
    doseage_multiplier = 1,
    df = 'Df',
    uu = 'Uu',
    app_flags = 1,
    timestmp = dt_now,
    sched2_no = 'SchedTwo',
    orig_expire_date = dt_now,
    rxq_status_cn = 1,
    IVRCmt = 'IVRCmt',
    wc_bodypart = 'WcBodypart',
    comp_ndc = 'CompNdc',
    treatment_yn = False,
    ivr_callback = 'IvrCallback',
    autofill_yn = False,
    autofill_resume_date = dt_now,
    worflow_status_cn = 1,
    extern_process_cn = 1,
    md_fac_id = 1,
    owner_store_id = 1,
    study_id = 1,
    min_days_until_refill = 1,
    sig_text_english = 'SigTextEnglish',
    order_fulfillment_cn = 1,
    taxable = 1,
    MAR_flag = 1,
    FreeFormStrength = 'FreeFormStrength',
    priority_cn = 1,
    ecs_yn = False,
    edit_locked_yn = False,
    locked_yn = False,
    locked_id = 1,
    locked_user_id = 1,
    daw_rx_cn = 1,
    add_user_id = 1,
    add_date = dt_now,
    chg_user_id = 1,
    chg_date = dt_now,
)

prescription_rnd = lambda cnt: mixer.cycle(cnt).blend(__model__)
