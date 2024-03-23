from odoo import models, fields, api, _

class LibraryBorrow(models.Model):
    _name = "library.borrow"
    
    _description = "for book check outs"


    ref = fields.Char(string = "Reference", default = lambda self: _("New"))
    person_id = fields.Many2one("res.partner", string="Patron")
    book_id = fields.Many2one("library.book", string="Book")
    #checkout_date = fields.Date("Date", compute="_compute_checkout_date")
    expected_return_date = fields.Date("Expected return")
    actual_return_date = fields.Date("Actual return")
    is_returned = fields.Boolean("Has returned ?", default=False)

    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            vals["ref"] = self.env["ir.sequence"].next_by_code('library.borrow')        
            book_id= vals["book_id"]
            book = self.env["library.book"].browse(book_id)
            book.qte -= 1
            history = self.env["library.history"]
            history.create({
                "ref": vals.get("ref"),
                "type": "borrow",
            })
            return super(LibraryBorrow,self).create(vals_list)
        
    @api.onchange("is_returned")
    def _onchange_is_returned(self):
        if (self.is_returned):
            book = self.book_id
            history = self.env["library.history"]
            history.create({
                "ref": self.ref,
                "type": "check_in",
            })
            book.qte += 1