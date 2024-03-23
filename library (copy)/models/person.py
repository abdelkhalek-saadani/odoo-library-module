from odoo import models, fields, api, _

class LibraryPerson(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    _description = "for person records"

    person_type = fields.Selection(string="Type",selection=[("patron","Patron"),("university","University")])
    personal_notes = fields.Text(string="Notes")
    cin = fields.Char(string="CIN")
    