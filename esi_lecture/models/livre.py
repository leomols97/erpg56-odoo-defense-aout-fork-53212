from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
import datetime

import logging

_logger = logging.getLogger(__name__)


###
### Book that contain all the thing
###

class Livre(models.Model):
    _name = 'esi.lecture.livre'
    _description = 'Un livre'
    name = fields.Char(string="Titre", default="", required=True)
    description = fields.Html(string="La description du livre", required=True)
    image = fields.Binary(string="Image de couverture")
    datePublication = fields.Date(string="Date de publication", required=True)
    numberOfPage = fields.Integer(string="Nombre de pages", default=1, required=True)
    auteur_id = fields.Many2many('res.partner', string="Auteurs/Name")

    like_user_id = fields.Many2many('res.users', string="Like")

    _sql_constraints = [('name_unique', 'unique(name)', 'Le livre doit être unique !')]
    _logger.info('------------------------------------\nDébut de applicaiton %s\n------------------------------------',
                 __name__)

    ### Contrainte sur le nombre de page qui doit être sup à 0
    @api.constrains('numberOfPage')
    def _check_numberofpage(self):
        for rec in self:
            if rec.numberOfPage <= 0:
                _logger.info(
                    '\n\n------------------------------------\nErreur nombre de page %s\n------------------------------------\n\n',
                    __name__)
                raise ValidationError('Le nombre de page doit être supérieur à 0')

    ### Contrainte sur la date de publication qui doit être infirieure à 0
    @api.constrains('datePublication')
    def _check_expiration_date(self):
        for rec in self:
            if rec.datePublication >= fields.Date.today():
                _logger.info(
                    '\n\n------------------------------------\nErreur date publication %s\n------------------------------------\n\n',
                    __name__)
                raise ValidationError('La date de publication doit être inférieure à aujourdui')


        ######################
        #### Smart Button ####
        ######################

    # on peut mettre @api.depends('like_user_id') si on stock le compteur

    ### Compte le nombre de like pour le livre
    def _compute_book_like_count(self):
        for book in self:
            book.number_like_book = len(book.like_user_id)

    ### Like et unlike les livres d'un user
    def like_unlike_a_book(self):
        for book in self:
            if book.search([('like_user_id', '=', self.env.uid), ('name', '=', book.name)]):
                book.like_user_id -= self.env.user
            else:
                book.like_user_id += self.env.user

    ### Met l'attribut has_been_like à un message spécifique si l'utilisateur à liké un livre sinon non
    def _has_been_like(self):
        for book in self:
            if book.search([('like_user_id', '=', self.env.user.id), ('name', '=', book.name)]):
                book.like_statut = "Vous avez aimé"
            else:
                book.like_statut = ""

    # On peut mettre store=True pour pouvoir si on le souhaite faire des filtre, recherche, etc
    number_like_book = fields.Integer(string="Likes", compute='_compute_book_like_count')
    like_statut = fields.Char(string="has been like ?", compute='_has_been_like')

    #############################
    #### Fin du Smart Button ####
    #############################
