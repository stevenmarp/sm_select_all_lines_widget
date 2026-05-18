# -*- coding: utf-8 -*-
{
    'name': 'All In One Select All Lines | Sale Order Lines | Purchase Lines | Invoice Lines | Manufacturing Lines | Inventory Lines',
    'version': '18.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Select all sale order, purchase, invoice, manufacturing, and inventory lines in one click',
    'description': """
All In One Select All Lines Widget for Odoo 18
==============================================
Select all document lines in one click for Sales, Purchase, Accounting,
Manufacturing, and Inventory.

This Odoo app adds a Select All button and row checkbox toggle to common
editable document lines. It helps users quickly select multiple order lines,
purchase lines, invoice lines, journal items, manufacturing component lines,
by-product lines, and stock operation lines.

Features:
- Select all sale order lines and quotation lines
- Select all purchase order lines and RFQ lines
- Select all invoice lines, vendor bill lines, and journal items
- Select all manufacturing component lines and by-product lines
- Select all inventory transfer operation lines
- Row checkbox toggle for select and unselect per line
- Reusable boolean field widget for custom list and one2many views
- Works with Odoo 18 Community and Enterprise

Usage:
<field name="your_boolean_field" widget="sm_select_all_boolean"/>

SEO Keywords:
select all order lines, select all sale order lines, select all purchase lines,
select all invoice lines, select all account lines, select all journal items,
select all manufacturing lines, select all inventory lines, select all stock moves,
odoo select all lines, odoo checkbox lines, odoo sale order line checkbox,
odoo purchase order line checkbox, odoo invoice line checkbox, odoo manufacturing
component checkbox, odoo inventory operation checkbox, odoo 18 select all widget,
odoo one2many select all, odoo editable list select all, all in one select all lines
    """,
    'author': 'Steven Marp',
    'website': 'https://apps.odoo.com/apps/modules/browse?repo_maintainer_id=512936',
    'license': 'OPL-1',
    'depends': ['sale', 'purchase', 'account', 'mrp', 'stock', 'web'],
    'data': [
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
        'views/account_move_views.xml',
        'views/mrp_production_views.xml',
        'views/stock_picking_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sm_select_all_lines_widget/static/src/js/select_all_boolean_field.js',
            'sm_select_all_lines_widget/static/src/xml/select_all_boolean_field.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 24.99,
    'currency': 'USD',
}
