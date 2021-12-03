from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    livre_lien_auteur = fields.Many2many('esi.lecture.livre', string='Livre dun auteur', default='')
    livre_nombre = fields.Integer(string="Nombre de livre", compute='_get_livre_nombre', store=True)
    isAuthor = fields.Boolean(string="Est un auteur ?", default=True)

    @api.depends('livre_nombre')
    def _get_livre_nombre(self):
        for auteur in self:
            auteur.livre_nombre = len(auteur.livre_lien_auteur)