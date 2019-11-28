# -*- coding: utf-8 -*-
from openerp import models, fields, tools


class PabiFutureCommitReport(models.Model):
    _name = 'pabi.future.commit.report'
    
    doc_number = fields.Char('doc_number')
    order_date = fields.Char('order_date')
    po_contract = fields.Char('po_contract')
    po_contract_type = fields.Char('po_contract_type')
    po_contract_start_date = fields.Char('po_contract_start_date')
    po_contract_end_date = fields.Char('po_contract_end_date')
    procurement_method = fields.Char('procurement_method')
    pr_reference = fields.Char('pr_reference')
    pd_reference = fields.Char('pd_reference')
    item = fields.Integer('item')
    product_name = fields.Char('product name')
    description = fields.Char('description')
    scheduled_date = fields.Char('scheduled_date')
    product_categ = fields.Char('product_categ')
    gl_code = fields.Char('gl_code')
    gl_name = fields.Char('gl_name')
    ag_code = fields.Char('ag_code')
    ag_name = fields.Char('ag_name')
    rpt_code = fields.Char('rpt_code')
    rpt_name = fields.Char('rpt_name')
    budget_view = fields.Char('budget_view')
    budget_code = fields.Char('budget_code')
    budget_name = fields.Char('budget_name')
    fund = fields.Char('fund')
    job_order = fields.Char('job_order')
    quantity = fields.Float('quantity', digits=(32, 2))
    uom = fields.Char('UOM')
    unit_price = fields.Float('unit_price', digits=(32, 2))
    taxes = fields.Char('taxes')
    subtotal = fields.Float('subtotal', digits=(32, 2))
    subtotal_th = fields.Float('subtotal th', digits=(32, 2))
    type_taxes = fields.Char('type_taxes')
    ex_in_clude = fields.Float('ex_in_clude', digits=(32, 2))
    total = fields.Float('total', digits=(32, 2))
    currency = fields.Char('currency')
    fiscalyear = fields.Char('fiscalyear')
    invoice_plan = fields.Char('invoice_plan')
    fin_lease = fields.Char('fin_lease')
    supplier_code = fields.Char('supplier_code')
    supplier_name = fields.Char('supplier_name')
    org_code = fields.Char('org_code')
    org_name = fields.Char('org_name')
    costcenter_code = fields.Char('costcenter_code')
    costcenter_name = fields.Char('costcenter_name')
    mission_name = fields.Char('mission_name')
    functional_area_code = fields.Char('functional_area_code')
    functional_area_name = fields.Char('functional_area_name')
    program_group_code = fields.Char('program_group_code')
    program_group_name = fields.Char('program_group_name')
    program_code = fields.Char('program_code')
    program_name = fields.Char('program_name')
    project_group_code = fields.Char('project_group_code')
    project_group_name = fields.Char('project_group_name')
    master_plan_code = fields.Char('master_plan_code')
    master_plan_name = fields.Char('master_plan_name')
    project_type_code = fields.Char('project_type_code')
    project_type_name = fields.Char('project_type_name')
    operation_code = fields.Char('operation_code')
    operation_name = fields.Char('operation_name')
    fund_type_code = fields.Char('fund_type_code')
    fund_type_name = fields.Char('fund_type_name')
    project_date_start = fields.Char('project_date_start')
    project_date_end = fields.Char('project_date_end')
    start_date_spending = fields.Char('start_spend')
    end_date_spending = fields.Char('end_spend')
    pm_code = fields.Char('pm_code')
    pm_name = fields.Char('pm_name')
    project_status = fields.Char('project_status')
    sector_code = fields.Char('sector_code')
    sector_name = fields.Char('sector_name')
    subsector_code = fields.Char('subsector_code')
    subsector_name = fields.Char('subsector_name')
    division_code = fields.Char('division_code')
    division_name = fields.Char('division_name')
    section_program_code = fields.Char('section_program_code')
    section_program_name = fields.Char('section_program_name')
    project_c_code = fields.Char('Project-C code')
    project_c_name = fields.Char('Project-C Name')
    pm_project_c_code = fields.Char('PM Project-C code')
    pm_project_c_name = fields.Char('PM Project-C Name')
    po_status = fields.Char('po_status')
    
    
    
    
    """invoice_line_id = fields.Many2one('account.invoice.line')
    activity_group_id = fields.Many2one('account.activity.group')
    activity_rpt_id = fields.Many2one('account.activity')
    contract_id = fields.Many2one('purchase.contract')
    currency_id = fields.Many2one('res.currency')
    fiscalyear_id = fields.Many2one('account.fiscalyear')
    invest_construction_phase_id = fields.Many2one('res.invest.construction.phase')
    operating_unit_id = fields.Many2one('operating.unit')
    partner_id = fields.Many2one('res.partner')
    po_contract_type_id = fields.Many2one('purchase.contract.type')
    product_categ_id = fields.Many2one('product.category')
    product_id = fields.Many2one('product.product')
    purchase_id = fields.Many2one('purchase.order')
    purchase_line_id = fields.Many2one('purchase.order.line')
    purchase_method_id = fields.Many2one('purchase.method')
    request_id = fields.Many2one('purchase.request')
    requisition_id = fields.Many2one('purchase.requisition')
    uom_id = fields.Many2one('product.uom')
    section_id = fields.Many2one('res.section')
    section_program_id = fields.Many2one('res.section.program')
    invest_asset_id = fields.Many2one('res.invest.asset')
    functional_area_id = fields.Many2one('res.functional.area')
    program_group_id = fields.Many2one('res.program.group')
    program_id = fields.Many2one('res.program')
    project_group_id = fields.Many2one('res.project.group')
    project_id = fields.Many2one('res.project')
    invest_construction_id = fields.Many2one('res.invest.construction')"""


class PabiFutureCommitSummaryReport(models.Model):
    _name = 'pabi.future.commit.summary.report'
    
    fiscalyear = fields.Char('fiscalyear')
    doc_number = fields.Char('doc_number')
    contract_number = fields.Char('contract_number')
    po_total = fields.Float('po_total', digits=(32, 2))
    po_commit = fields.Float('po_commit', digits=(32, 2))
    po_actual = fields.Float('po_actual', digits=(32, 2))
    remaining = fields.Float('remaining', digits=(32, 2))
    budget_view = fields.Char('budget_view')
    budget_code = fields.Char('budget_code')
    budget_name = fields.Char('budget_name')
    po_status = fields.Char('po_status')
    close_uncommit = fields.Boolean('close_uncommit')
    
    
    
    