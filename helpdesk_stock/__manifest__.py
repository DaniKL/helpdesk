# Copyright 2019 Daniel Cano, Adrián Cruz, María Alhambra
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "HelpDesk Stock",
    "summary": "Module to Support Teams",
    "version": "12.0.1.0.0",

    "category": "Customer Relationship Management",
    "website": "",
    "author": "Daniel Cano Lozoya,"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "data": [
        "views/stock_picking_view.xml",
        "views/helpdesk_ticket_view.xml",
        "wizard/stock_return_picking_view.xml"
    ],
    "application": True,
    "installable": True,
    "depends": ["helpdesk", "stock", "base", "mail"],
}
