import logging

import pyisbn
from odoo import models, fields, api, exceptions, _

_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'kw.lib.book'
    _description = 'Book'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
    isbn = fields.Char(
        required=True, )
    author_ids = fields.Many2many(
        comodel_name='kw.lib.author', )
    category_id = fields.Many2one(
        comodel_name='kw.lib.book.category', )

    @api.constrains('author_ids')
    def _constrains_author_ids(self):
        for obj in self:
            if not obj.author_ids:
                raise exceptions.ValidationError(_('Author is required'))

    @api.constrains('isbn')
    def _constrains_isbn(self):
        for obj in self:
            try:
                if not pyisbn.validate(obj.isbn):
                    raise exceptions.ValidationError(_('ISBN is not valid'))
            except Exception as e:
                raise exceptions.ValidationError(e)


class BookInstance(models.Model):
    _name = 'kw.lib.book.instance'
    _description = 'Book instance'
    _inherits = {'kw.lib.book': 'book_id'}

    book_id = fields.Many2one(
        comodel_name='kw.lib.book', required=True, )
    code = fields.Char(
        copy=False, readonly=True, )

    @api.model
    def create(self, vals_list):
        vals_list['code'] = self.env['ir.sequence'].next_by_code(
            'kw.lib.book.instance')
        return super().create(vals_list)
