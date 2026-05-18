# -*- coding: utf-8 -*-
from odoo import models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def sm_select_all_raw_moves(self):
        for production in self:
            production.move_raw_ids.write({'sm_check_ok': True})
        return True

    def sm_select_all_byproduct_moves(self):
        for production in self:
            production.move_byproduct_ids.write({'sm_check_ok': True})
        return True
