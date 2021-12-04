
from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
import datetime

import logging

_logger = logging.getLogger(__name__)


class Livre(models.Model):
    _name = 'esi.lecture.livre'
    _description = 'Un livre'
    name = fields.Char(string="Titre", default="", required=True)
    description = fields.Html(string="La description du livre", required=True)
    image = fields.Binary(string="Image de couverture")
    datePublication = fields.Date(string="Date de publication", required=True)
    numberOfPage = fields.Integer(string="Nombre de pages", default=1, required=True)
    auteur_id = fields.Many2many('res.partner', String="Auteurs/Name")
    _sql_constraints = [('name_unique', 'unique(name)', 'Le livre doit être unique !')]
    _logger.info('------------------------------------\nDébut de applicaiton %s\n------------------------------------',
                 __name__)

    @api.constrains('numberOfPage')
    def _check_numberofpage(self):
        for rec in self:
            if rec.numberOfPage <= 0:
                raise ValidationError('Le nombre de page doit être supérieur à 0')

    @api.constrains('datePublication')
    def _check_expiration_date(self):
        for rec in self:
            if rec.datePublication >= fields.Date.today():
                raise ValidationError('La date de publication doit être inférieure à aujourdui')
