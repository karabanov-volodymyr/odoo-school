import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Author(models.Model):
    _name = 'kw.lib.author'
    _description = 'Author'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
