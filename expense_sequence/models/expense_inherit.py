from odoo import fields, models, api, _

class Discount(models.Model):
    _inherit = 'hr.expense'

    @api.depends('employee_id')
    def _compute_is_ref_editable(self):
        is_account_manager = self.env.user.has_group('account.group_account_user') or self.env.user.has_group(
            'account.group_account_manager') or self.env.user.has_group(
            'account.group_account_invoice')
        for expense in self:
            if expense.state == 'draft' or expense.sheet_id.state in ['draft', 'submit']:
                expense.is_ref_editable = True
            else:
                expense.is_ref_editable = is_account_manager





