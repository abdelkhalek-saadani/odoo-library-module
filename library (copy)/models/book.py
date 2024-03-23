from odoo import models, fields, api, _

class LibraryBook(models.Model):
    _name = "library.book"
    
    _description = "for book records"

    ref = fields.Char(string="Reference", default=lambda self: _("New"))
    name = fields.Char(string = "Title", required = True)
    cover = fields.Binary()
    pages = fields.Integer(string="Number of pages")
    qte = fields.Integer(string="Available books", required = True)
    author_ids = fields.Many2many("library.author",
                                  string="Authors")
    authors = fields.Char(compute ="_compute_authors")
    price = fields.Integer(string= "Price",required=False, default=0)
    purchase_price = fields.Integer(string= "Cost")
    is_used = fields.Boolean(string="To get borrowed?",default="False", required= True)
    category_id = fields.Many2one("library.category", string="Category")
    active = fields.Boolean(default="True")

    @api.model_create_multi
    def create(self, vals_list):
        history = self.env["library.history"]
        for vals in vals_list:
            vals["ref"] = self.env["ir.sequence"].next_by_code('library.book')
            history.create({
                "ref": vals["ref"],
                "type": "new_book",
                "qte_to": vals["qte"],
                "price_to": vals["price"],
                "cost_to": vals["purchase_price"]
            })
        return super(LibraryBook, self).create(vals_list)


    def write(self, values):
        history = self.env["library.history"]
        for rec in self:
            if values.get("qte",None):
                history.create({
                    "ref": rec.ref,
                    "type": "buy",
                    "qte_to": values["qte"] - rec.qte
                })
            if values.get("purchase_price",0) or values.get("price",0):
                history.create({
                    "ref": rec.ref,
                    "type": "cost_price",
                    "cost_to": values.get("purchase_price",0),
                    "price_to": values.get("price",0)
                })

        return super(LibraryBook, self).write(values)

    def name_get(self):
        res=[]
        for rec in self:
            new_name = f'{rec.name} By {rec.authors} ({rec.pages}page)'
            res.append((rec.id,new_name))
        return res
    
    @api.depends("author_ids")
    def _compute_authors(self):
        for rec in self:
            rec.authors=""
            for author in rec.author_ids:
                rec.authors = author.name + ", " + rec.authors 
            rec.authors = rec.authors[:-2]
