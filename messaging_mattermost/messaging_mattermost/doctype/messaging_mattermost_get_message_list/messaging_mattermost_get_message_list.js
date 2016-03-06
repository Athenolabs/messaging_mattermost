// Copyright (c) 2016, Semilimes and contributors
// For license information, please see license.txt

frappe.ui.form.on('Messaging Mattermost Get Message List', {
	refresh: function(frm) {

	},
	get_messages: function(frm, cdt, cdn){
        var doc = frappe.model.get_doc(cdt, cdn);

		//noinspection SpellCheckingInspection
        frappe.call({
            method: "messaging_mattermost.messaging_mattermost.doctype." +
                "messaging_mattermost_get_message_list.messaging_mattermost_get_message_list.get_message_list",
			callback: function(r) {
				frappe.model.set_value(cdt, cdn, "message_list", r.message);
			}
		});
    }
});
