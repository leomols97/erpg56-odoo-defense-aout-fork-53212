from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
import datetime

import logging

_logger = logging.getLogger(__name__)

class Livre(models.Model):
    _name = 'esi.lecture.livre'
    _description = 'Un livre'
    name = fields.Char(string="Nom du livre", default="", required=True)
    description = fields.Text(string="La description du livre", default="")
    image = fields.Binary(string="Image de couverture")
    datePublication = fields.Date(string="Date de publication")
    numberOfPage = fields.Integer(string="Nombre de page", default=1)
    auteur_id = fields.Many2many('res.partner', String="Auteurs", default="")
    _sql_constraints = [('name_unique', 'unique (name)', 'Le livre doit être unique !')]
    _logger.info('------------------------------------\nDébut de applicaiton %s\n------------------------------------', __name__)


@api.constrains('numberOfPage')
def _check_numberofpage(self):
    if self.numberOfPage <= 0:
        raise ValidationError('Le nombre de page doit être supérieur à 0')

@api.constrains('datePublication')
def _check_expiration_date(self):
    if self.datePublication >= datetime.today():
        raise ValidationError('La date de publication doit être inférieure à aujourdui')