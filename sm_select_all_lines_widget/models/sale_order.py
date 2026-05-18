# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def sm_select_all_order_lines(self):
        for order in self:
            order.order_line.filtered(lambda line: not line.display_type).write({'sm_check_ok': True})
        return True


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sm_check_ok = fields.Boolean(string='Select', default=False, copy=False)

    def sm_action_toggle_select(self):
        for line in self:
            line.sm_check_ok = not line.sm_check_ok
        return True
