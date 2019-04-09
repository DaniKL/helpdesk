# Copyright 2019 Daniel Cano, María Alhambra, Adrián Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HelpdeskStock(models.Model):
    _name = 'helpdesk.stock'
    _description = 'Helpdesk Stock'

    ticket_id = fields.Many2one(
        string="Ticket",
        comodel_name="helpdesk.ticket")

    return_id = fields.Many2one(
        string="Return",
        comodel_name="stock.picking")
