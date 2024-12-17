{
    "name" : "Library",
    "author" : "Abdelkhalek at CapIT",
    "summary" : "Manage library's Books sales, purchases and check outs",
    "depends" : ["mail","product","stock"],
    "data" : [
        "security/ir.model.access.csv",
        "data/sequence.xml",

        "views/person.xml",
        "views/menu.xml",
        "views/book.xml",
        "views/order.xml",
        "views/order_line.xml",
        "views/borrow.xml",
        "views/history.xml"
    ],
    'installable': True,
    'application': True,
}