from odoo import fields, models, api


class ModelName(models.Model):
    _inherit = 'hr.employee'

    parent_id = fields.Many2one('hr.employee', 'Manager', compute="_compute_parent_id", store=True, readonly=False,
                                domain="[]")
