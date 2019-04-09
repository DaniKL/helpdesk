# Copyright 2019 Daniel Cano, María Alhambra, Adrián Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HelpdeskActions(models.Model):
    _name = 'helpdesk.actions'
    _description = 'Helpdesk Actions'

    name = fields.Char()

    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='Ticket')

    '''
    ticket_ids = fields.One2many(
        comodel_name='helpdesk.ticket',
        inverse_name='actions_id',
        string='Ticket')
    '''
