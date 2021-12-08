from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
import datetime

import logging

_logger = logging.getLogger(__name__)

class Product(models.Model):
    _inherit = 'product.template'
    list_book_product = fields.Many2many('esi.lecture.livre', string="Liste de livres")
    list_book_count = fields.Integer(string='Nombre de livre', compute='_get_number_book', store=True)

    @api.depends('list_book_product')
    def _get_number_book(self):
        for book in self:
            book.list_book_count = len(book.list_book_product)
