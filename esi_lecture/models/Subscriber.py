from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import datetime

import logging

_logger = logging.getLogger(__name__)


class Subscriber(models.Model):
    _inherit = 'res.partner'
    is_subscriber = fields.Boolean('Can write reviews ?', default = False)
    review_ids = fields.One2many('esi.lecture.livre.review.xml', 'subscriber_id')
