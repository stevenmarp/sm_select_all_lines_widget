# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def sm_select_all_invoice_lines(self):
        for move in self:
            move.invoice_line_ids.filtered(
                lambda line: line.display_type not in ('line_section', 'line_note')
            ).write({'sm_check_ok': True})
        return True

    def sm_select_all_journal_items(self):
        for move in self:
            move.line_ids.filtered(
                lambda line: line.display_type not in ('line_section', 'line_note')
            ).write({'sm_check_ok': True})
        return True


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    sm_check_ok = fields.Boolean(string='Select', default=False, copy=False)

    def sm_action_toggle_select(self):
        for line in self:
            line.sm_check_ok = not line.sm_check_ok
        return True
