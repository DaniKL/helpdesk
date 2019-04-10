# Copyright 2019 Daniel Cano, María Alhambra, Adrián Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    ticket_id = fields.Many2one(
        string="Stock Picking",
        comodel_name="helpdesk.ticket"
    )
