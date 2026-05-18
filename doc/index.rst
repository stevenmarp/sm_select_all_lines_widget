=======================
Select All Lines Widget
=======================

.. contents::
   :local:
   :depth: 2

Overview
========

``sm_select_all_lines_widget`` adds a select-all workflow to editable
document lines in Odoo 18.

Users can click **Select All** above supported line tabs, then toggle
individual rows with a compact checkbox icon.

Covered Apps
============

The module extends these standard Odoo documents:

* Sales Orders and Quotations
* Purchase Orders and RFQs
* Customer Invoices, Vendor Bills, and Journal Entries
* Manufacturing Orders
* Inventory Transfers

Features
========

* Select-all button above supported one2many line widgets.
* Row-level toggle button with selected and unselected icons.
* Hidden boolean field to store selected state on each line.
* ``copy=False`` on selection fields, so duplicated records do not keep
  old selections.
* Reusable backend boolean widget named ``sm_select_all_boolean``.

Technical Scope
===============

Models extended
---------------

* ``sale.order`` and ``sale.order.line``
* ``purchase.order`` and ``purchase.order.line``
* ``account.move`` and ``account.move.line``
* ``mrp.production``
* ``stock.picking``
* ``stock.move``
* ``stock.move.line``

Views extended
--------------

* Sales order form
* Purchase order form
* Account move form
* Manufacturing order form
* Stock picking form

Reusable Widget
===============

The module also registers a reusable boolean list widget:

.. code-block:: xml

   <field name="your_boolean_field" widget="sm_select_all_boolean"/>

When used on a boolean field in a list view, the header can toggle all
editable visible rows for that boolean field.

Installation
============

1. Copy ``sm_select_all_lines_widget`` into an Odoo addons path.
2. Restart Odoo.
3. Update the Apps list.
4. Install **Select All Lines Widget**.

Command-line install or update:

.. code-block:: bash

   python3 ~/odoo/odoo-18/odoo-server \
      -c ~/odoo/conf/unotek.conf \
      -d uno_db_fresh \
      -u sm_select_all_lines_widget

Dependencies
============

The module depends on:

* ``sale``
* ``purchase``
* ``account``
* ``mrp``
* ``stock``
* ``web``

Usage
=====

1. Open a supported document form.
2. Open its line tab, such as Order Lines, Invoice Lines, Components, or
   Operations.
3. Click **Select All**.
4. Use the row checkbox icon to unselect or reselect specific lines.

Compatibility
=============

* Odoo 18.0
* Community and Enterprise editions

Changelog
=========

18.0.1.0.0
----------

* Initial release.
* Added select-all controls for Sales, Purchase, Accounting,
  Manufacturing, and Inventory lines.
* Added reusable ``sm_select_all_boolean`` field widget.
