from odoo import models, fields, api, _

class LibraryOrder(models.Model):
    _name = "library.order"
    
    _description = "desc"

    ref = fields.Char(string = "Reference", default = lambda self: _("New"))
    person_id = fields.Many2one("res.partner")
    order_line_ids = fields.One2many("library.order_line", "order_id")
    total_price = fields.Float("Total", compute="_compute_total_price")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals["ref"] = self.env["ir.sequence"].next_by_code('library.order')
            for order_line in vals.get('order_line_ids', []):
                book_id = order_line[2].get('book_id')
                quantity = order_line[2].get('qte')
                if book_id and quantity:
                    book = self.env["library.book"].browse(book_id)
                    book.qte -= quantity
            history = self.env["library.history"]
            history.create({
                "ref": vals["ref"],
                "type": "order",
            })
        return super(LibraryOrder, self).create(vals_list)


    def write(self, vals):
        history = self.env["library.history"]
        for rec in self:
            history.create({
                "ref": rec.ref,
                "type": "order",
            })
        return super(LibraryOrder, self).write(vals)

    @api.depends("order_line_ids")
    def _compute_total_price(self):
        for rec in self:
            rec.total_price = 0
            for order_line in rec.order_line_ids:
                rec.total_price += order_line.total_price