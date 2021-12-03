from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    auteur_ids = fields.Many2many('esi_lecture.livre', 'auteur_id', string='Auteur livre', default='')