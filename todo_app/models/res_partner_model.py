from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    todo_ids = fields.Many2many('todo.task', 'team_ids', string='To-do Teams', default='')