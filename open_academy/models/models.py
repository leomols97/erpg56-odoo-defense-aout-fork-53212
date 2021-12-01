# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields

class Course(models.Model):
    _name = 'openacademy.course'
    name = fields.Char(string="Title", required=True)
    description = fields.Text()


# class open_academy(models.Model):
#     _name = 'open_academy.open_academy'
#     _description = 'open_academy.open_academy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
