from odoo import models, fields, api, exceptions

import logging

_logger = logging.getLogger(__name__)

class TodoTask(models.Model):
    _name = 'todo.task'
    _inherit = 'todo.task'
    effort_estimate = fields.Integer(string="temps estimé pour réaliser la tache", default="")
    tag_ids = fields.Many2many('todo.task.tag', String="Tags" , default="")
    desc = fields.Char(string="décrit brièvement la tâche", default="")
    state = fields.Selection([('draft', 'Nouveau'), ('open', 'Ouvert/Commencé'), ('done', 'Fermé')],string="etat possible d'une tâche" ,default='draft')
    docs = fields.Html('Documentation')
    date_created = fields.Datetime('DateCreationTache', default = lambda self: fields.datetime.now())
    image = fields.Binary('imageTache')