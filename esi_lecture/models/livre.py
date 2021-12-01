from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
import datetime

import logging

_logger = logging.getLogger(__name__)

class Livre(models.Model):
    _name = 'esi_lecture.livre'
    _description = 'Un livre'
    name = fields.Char(string="nom de la tâche", default="", required=True)

    description = fields.Char(string="La description du livre", default="")
    image = fields.Binary(string="Image de couverture")
    datePublication = fields.Date(string="Date de publication")
    numberOfPage = fields.Integer(string="Nombre de page")
    auteur_id = fields.Many2many('res.partner', String="Auteur", default="")
    _sql_constraints = [('name_unique', 'unique (name)', 'Le livre doit être unique !')]
    _logger.info('------------------------------------\nDébut de applicaiton %s\n------------------------------------', __name__)


@api.constrains('numberOfPage')
def _check_numberofpage(self):
    if self.numberOfPage > 0:
        raise ValidationError('Le nombre de page doit être supérieur à 0')

@api.constrains('datePublication')
def _check_expiration_date(self):
    if self.datePublication >= datetime.today():
        raise ValidationError('La date de publication doit être inférieure à aujourdui')