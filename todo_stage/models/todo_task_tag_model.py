from odoo import models, fields, api, exceptions

import logging

_logger = logging.getLogger(__name__)

class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-do Tag'
    name = fields.Char(string="nom du tag", default="")
    task_ids = fields.Many2many("todo.task", String="Tags relation", default="")