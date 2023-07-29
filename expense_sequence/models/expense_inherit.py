from odoo import fields, models, api, _


class ExpenseSequence(models.Model):
    _inherit = 'hr.expense'

    # sequence_number = fields.Char(
    #     string="Expense Number",
    #     required=True, copy=False,
    #     readonly=True,
    #     default=lambda self: _('EXP'))

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

    # @api.model
    # def create(self, vals):
    #     if vals.get('sequence_number', _('EXP')) == _('EXP'):
    #         vals['sequence_number'] = self.env['ir.sequence'].next_by_code('hr.expense.invoice') or _('EXP')
    #     return super(ExpenseSequence, self).create(vals)
