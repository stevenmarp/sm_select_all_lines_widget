/** @odoo-module **/

import { registry } from "@web/core/registry";
import { patch } from "@web/core/utils/patch";
import { booleanField } from "@web/views/fields/boolean/boolean_field";
import { ListRenderer } from "@web/views/list/list_renderer";

export const selectAllBooleanField = {
    ...booleanField,
    listViewWidth: 72,
};

registry.category("fields").add("sm_select_all_boolean", selectAllBooleanField);
registry.category("fields").add("list.sm_select_all_boolean", selectAllBooleanField);

patch(ListRenderer.prototype, {
    getSelectAllBooleanRecords(column) {
        if (this.props.list.isGrouped) {
            return [];
        }
        return this.props.list.records.filter((record) => !this.isCellReadonly(column, record));
    },

    getSelectAllBooleanValue(column) {
        const records = this.getSelectAllBooleanRecords(column);
        return records.length > 0 && records.every((record) => record.data[column.name]);
    },

    async toggleSelectAllBoolean(column, value) {
        const records = this.getSelectAllBooleanRecords(column);
        await Promise.all(records.map((record) => record.update({ [column.name]: value })));
    },
});
