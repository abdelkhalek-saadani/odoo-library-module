from odoo import models, fields, api, _

class LibraryAuthor(models.Model):
    _name = "library.author"
    _description = "for author records"

    name = fields.Char(string = "Name", required = True, tracking=True)
    date_of_birth = fields.Date(string="Date of Birth")
    birthplace = fields.Char(string="Birthplace")