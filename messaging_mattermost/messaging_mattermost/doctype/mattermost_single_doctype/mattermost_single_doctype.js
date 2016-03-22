// Copyright (c) 2016, Semilimes and contributors
// For license information, please see license.txt

frappe.ui.form.on('Mattermost Single DocType', {
	refresh: function(frm) {

	},
    send: function(frm, cdt, cdn){
		var doc = frappe.model.get_doc(cdt, cdn);

		////noinspection SpellCheckingInspection
        frappe.call({
            method: "messaging_mattermost.messaging_mattermost.doctype.mattermost_single_doctype." +
			"mattermost_single_doctype.send_message",
			args: {
                message: doc.message
			}
		});
		frappe.call({
            method: "messaging_mattermost.messaging_mattermost.doctype." +
                "mattermost_single_doctype.mattermost_single_doctype.get_message_list",
			callback: function(r) {
				frappe.model.set_value(cdt, cdn, "message_list", r.message);
			}
		});
    }
});
