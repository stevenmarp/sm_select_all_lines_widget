# -*- coding: utf-8 -*-
from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def sm_select_all_moves(self):
        for picking in self:
            picking.move_ids_without_package.write({'sm_check_ok': True})
        return True

    def sm_select_all_move_lines(self):
        for picking in self:
            picking.move_line_ids.write({'sm_check_ok': True})
        return True


class StockMove(models.Model):
    _inherit = 'stock.move'

    sm_check_ok = fields.Boolean(string='Select', default=False, copy=False)

    def sm_action_toggle_select(self):
        for move in self:
            move.sm_check_ok = not move.sm_check_ok
        return True


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    sm_check_ok = fields.Boolean(string='Select', default=False, copy=False)

    def sm_action_toggle_select(self):
        for move_line in self:
            move_line.sm_check_ok = not move_line.sm_check_ok
        return True
