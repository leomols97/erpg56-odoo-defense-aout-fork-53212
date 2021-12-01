from odoo import models, fields, api, exceptions

import logging

_logger = logging.getLogger(__name__)

class TodoTask(models.Model):
    _name = 'todo.task'
    name = fields.Char(string="nom de la tâche", default="", required=True)
    is_done = fields.Boolean(string="est à vrai si la tâche est terminée", default="")
    active = fields.Boolean(string="seul les taches actives seront affichées", default=1)
    date_deadline = fields.Date(string="date de fin de la tâche", default="")
    user_id = fields.Many2one('res.users', String="Responsible" , default= lambda self: self.env.user)
    team_ids = fields.Many2one('res.partner', String="Team", default="")
    _logger.info('------------------------------------\nDébut de applicaiton %s\n------------------------------------', __name__)

    def do_clear_done(self):
        for task in self:
            if task.active:
                task.active = False
                _logger.info('------------------------------------\nLa tâche est passé de actif à inactif\n------------------------------------')
            else:
                raise exceptions.Warning("La tache est déjà inacive")
        return True

    def write(self, values):
        if 'active' not in values:
            values['active'] = True
            _logger.info('------------------------------------\nLa tâche était inactif mais est passé à actif en modifiant ses valeurs\n------------------------------------')
        return super(TodoTask, self).write(values)

    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(TodoTask, self).copy(default)

    def __str__(self):
        return f"Task(id={self.id}, name={self.name}, is_done={self.is_done}, active={self.active}, data_deadline={self.date_deadline}, user_name={self.user_id.name}, team_count={len(self.team_ids)}"

