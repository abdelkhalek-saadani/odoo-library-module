from odoo import http
from odoo.http import request
import json

class ListBooksController(http.Controller):
    @http.route(['/books/'], type="http", auth="public", website="True")
    def list_books(self, **kw):
        books = request.env['library.book'].sudo().search([])
        books_json = []
        print(kw)
        print(kw.get("param1"))
        for key, value in kw.items():
            print(key)
            print(value)
        for book in books:
            element = {
                "title": book.name,
                "page_numbers": book.pages
            }
            books_json.append(element)

        return json.dumps(books_json)

    @http.route(['/add_book/'], type="http", auth="public", website="True")
    def list_books(self, **kw):
        book = {
            "name":"book_3",
            "qte":10
        }
        request.env["library.book"].create(book)
        json_res = {
            "msg": "book added successfully!"
        }
        return json.dumps(json_res)