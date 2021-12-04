from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tests.common import TransactionCase
from odoo import exceptions

import datetime
import logging

_logger = logging.getLogger(__name__)


class TestBook(TransactionCase):

    def test_create(self):
        "Create a simple Book"
        book = self.env['esi.lecture.livre']
        books = book.create(
            {'name': 'Coco le nouveau', 'description': '<h1>Quatrième de couverture</h1><br><p>Coucou</p>',
             'numberOfPage': 231, 'datePublication': '2021-01-01'})
        self.assertEqual(books.name, 'Coco le nouveau')
        self.assertEqual(books.description, '<h1>Quatrième de couverture</h1><br><p>Coucou</p>')
        self.assertEqual(books.image, False)
        self.assertEqual(books.numberOfPage, 231)
        self.assertEqual(books.datePublication, datetime.date(2021, 1, 1))
        self.assertEqual(len(books.auteur_id), 0)

        _logger.info(
            '\n\n------------------------------------\nTest création classique %s\n------------------------------------\n\n',
            __name__)

    def test_create_error_numberPage(self):
        "Create a simple Book"
        book = self.env['esi.lecture.livre']
        with self.assertRaises(ValidationError):
            task = book.create(
                {'name': 'Coco le nouveau', 'description': '<h1>Quatrième de couverture</h1><br><p>Coucou</p>',
                 'datePublication': '2021-01-01', 'numberOfPage': 0})

        _logger.info(
            '\n\n------------------------------------\nTest error nombre de page %s\n------------------------------------\n\n',
            __name__)

    def test_create_error_datePublication(self):
        "Create a simple Book"
        book = self.env['esi.lecture.livre']
        with self.assertRaises(ValidationError):
            task = book.create(
                {'name': 'Coco le nouveau', 'description': '<h1>Quatrième de couverture</h1><br><p>Coucou</p>',
                 'datePublication': '2100-12-12', 'numberOfPage': 31})

        _logger.info(
            '\n\n------------------------------------\nTest error date de publication %s\n------------------------------------\n\n',
            __name__)

    def test_create_with_autor(self):
        "Create a simple Book"
        book = self.env['esi.lecture.livre']
        books = book.create(
            {'name': 'Coco le nouveau', 'description': '<h1>Quatrième de couverture</h1><br><p>Coucou</p>',
             'numberOfPage': 231, 'datePublication': '2021-01-01', 'auteur_id': self.env['res.partner'].create({'name': 'bobi', 'is_author': True, })})
        self.assertEqual(books.name, 'Coco le nouveau')
        self.assertEqual(books.description, '<h1>Quatrième de couverture</h1><br><p>Coucou</p>')
        self.assertEqual(books.image, False)
        self.assertEqual(books.numberOfPage, 231)
        self.assertEqual(books.datePublication, datetime.date(2021, 1, 1))
        self.assertEqual(len(books.auteur_id), 1)
        self.assertEqual(books.auteur_id[0].name, 'bobi')
        _logger.info(
            '\n\n------------------------------------\nTest création classique avec un autheur %s\n------------------------------------\n\n',
            __name__)
