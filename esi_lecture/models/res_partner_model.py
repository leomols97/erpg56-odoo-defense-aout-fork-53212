from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)

### Overide res.partner pour pouvoir avoir des auteurs
class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_author = fields.Boolean(string="Est un auteur ?", default=False)
    livre_lien_auteur = fields.Many2many('esi.lecture.livre',string="Livre d'un auteur")

    # On met store pour stocker la donnée dans la bd (par exemple : pour filtrer le tout)
    livre_nombre = fields.Integer(string="Nombre de livre", compute='_get_livre_nombre', store=True)

    ### Nombre de livre qui sont écrit pour un auteur
    @api.depends('livre_lien_auteur')
    def _get_livre_nombre(self):
        for auteur in self:
            auteur.livre_nombre = len(auteur.livre_lien_auteur)
