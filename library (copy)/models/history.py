from odoo import models, fields, api, _
from datetime import datetime


class LibraryHistory(models.Model):
    _name = "library.history"

    _description = "to track history "

    date = fields.Datetime(string='Date', default=lambda self: datetime.now())
    ref = fields.Char("Object reference")
    type = fields.Selection([
        ("buy", "Buy"),
        ("new_book", "New Book"),
        ("cost_price", "Cost or Price"),
        ("order", "Order"),
        ("borrow", "Borrow"),
        ("check_in", "Check In")
    ],
        "Type")
    qte_to = fields.Integer("Quantity changed to", default=0)
    price_to = fields.Float("Price changed to", default=0)
    cost_to= fields.Float("Cost changed to", default=0)