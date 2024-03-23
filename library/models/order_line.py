from odoo import models, fields, api, _

class LibraryOrderLine(models.Model):
    _name = "library.order_line"
    
    _description = "desc"

    
    order_id = fields.Many2one("library.order")
    book_id = fields.Many2one("library.book", string="Book")
    qte = fields.Integer(string="Quantity")
    unit_price = fields.Float(string="Unit Price", compute="_compute_unit_price")
    total_price = fields.Float(string="Total", compute="_compute_total_price")


    @api.depends("qte","book_id")
    def _compute_total_price(self):
        for rec in self:
            if len(rec.book_id)>=1:
                rec.total_price = rec.qte * rec.book_id[0].price
            else :
                rec.total_price =0

    @api.depends("book_id")
    def _compute_unit_price(self):
        for rec in self:
            if len(rec.book_id)>=1:
                rec.unit_price = rec.book_id[0].price
            else :
                rec.unit_price =0