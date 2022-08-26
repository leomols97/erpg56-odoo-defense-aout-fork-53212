from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import datetime

import logging
_logger = logging.setLogger(__name__)

class Review(models.Model):
    _name = 'esi.lecture.livre.review.xml'
    _description = 'Avis de livres'
    book_id = fields.Many2one('esi.lecture.livre', string="Livre prêté", required=True)
    subscriber_id = fields.Many2one('res.partner', string='Membre à l\'origine de l\'avis', required=True, default='_get_current_user')
    state = fields.Selection([('lecture', 'En cours de lecture'), ('finished', 'Terminé')], default='lecture')
    end_date = fields.Date(string='Date de fin de lecture', defaumt=datetime.today())
    rating = fields.Integer(default=0)

    @api.constrains('book_id')
    def _check_two_reviews_same_book(self):
        for review in self:
            for book in review.book_id:
                for review in book.review_id:
                    if review.name_book == self.name_book:
                        raise ValidationError('Vous avez déjà critiqué ce livre')

    @api.depends('book_id')
    def _get_name_book(self):
        self.name_book = self.book_id.name