from odoo import fields, models

class LibraryCategory(models.Model):
    _name="library.category"
    _description="book categories"

    name=fields.Char(string="Category name", required="true")
    book_ids = fields.One2many("library.book","category_id", string="Books",)