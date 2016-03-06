// Copyright (c) 2016, Semilimes and contributors
// For license information, please see license.txt

frappe.ui.form.on('Messaging Mattermost Send Message', {
	refresh: function(frm) {

	},
	send_message: function(frm, cdt, cdn){
        var doc = frappe.model.get_doc(cdt, cdn);

		//noinspection SpellCheckingInspection
        frappe.call({
            method: "messaging_mattermost.messaging_mattermost.doctype." +
                "messaging_mattermost_send_message.messaging_mattermost_send_message.send_message",
			args: {
                message: doc.message
			}
		});
    }
});