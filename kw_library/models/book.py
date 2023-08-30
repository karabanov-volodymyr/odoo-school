import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'kw.lib.book'
    _description = 'Book'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
    isbn = fields.Char()

    author_ids = fields.Many2many(
        comodel_name='kw.lib.author', )
    author_qty = fields.Integer(
        compute='_compute_author_qty', )

    def _compute_author_qty(self):
        for obj in self:
            obj.author_qty = len(obj.author_ids.ids)
