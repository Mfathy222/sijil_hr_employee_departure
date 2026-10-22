from odoo import fields, models  # noqa: I001

class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    currency_id = fields.Many2one(
        related="company_id.currency_id",
        readonly=True,
    )
    
    employee_accrued = fields.Monetary(
        string="Employee Accrued",
        related="version_id.employee_accrued",
        currency_field="currency_id",
        readonly=False,
    )
    
    account_accrued_id = fields.Many2one(
        comodel_name="account.account",
        string="Accrued Account",
        ondelete="restrict",
    )
    




            
    def action_print_employee_departure(self):
        partner_id = self.work_contact_id
        account_accrued = self.account_accrued_id
        if partner_id and account_accrued:
            domain = [
                    ('partner_id', '=', partner_id.id),
                    ('account_id', '=', account_accrued.id),
                    ('parent_state', '=', 'posted'),
                    ]
            move_lines = self.env['account.move.line'].search(domain)
            self.employee_accrued = abs(sum(move_lines.mapped('balance')))
        else:
            self.employee_accrued = 100
        return self.env.ref(
            'sijil_hr_employee_departure.action_report_departure_ams'
        ).report_action(self)
        
        
        
class HrVersion(models.Model):
    _inherit = "hr.version"

    employee_accrued = fields.Monetary(
        string="Employee Accrued",
        currency_field="currency_id",
        tracking=True,
        copy=False,
    )
    
    contract_number = fields.Char(
    string="Contract Number",
    readonly=False,
    )