// Copyright (c) 2016, gsn and contributors
// For license information, please see license.txt

frappe.ui.form.on('Manual Backup', {
	refresh: function(frm) {
		return frappe.call({
			doc: frm.doc,
			method: "update_cost",
			freeze: true,
			callback: function(r) {
				if(!r.exc) frm.refresh_fields();
			}
		})

	}
});
