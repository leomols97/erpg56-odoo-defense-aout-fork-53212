# -*- coding: utf-8 -*-
# from odoo import http


# class TodoStage(http.Controller):
#     @http.route('/todo_stage/todo_stage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_stage/todo_stage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_stage.listing', {
#             'root': '/todo_stage/todo_stage',
#             'objects': http.request.env['todo_stage.todo_stage'].search([]),
#         })

#     @http.route('/todo_stage/todo_stage/objects/<model("todo_stage.todo_stage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_stage.object', {
#             'object': obj
#         })
