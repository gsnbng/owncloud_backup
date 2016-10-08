# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import frappe
from frappe import _

default_mail_footer = """<div style="padding: 7px; text-align: right; color: #888"><small>Sent via
	<a style="color: #888" href="http://erpnext.org">ERPNext</a></div>"""

def before_install():
	if not os.path.exists(os.path.join(frappe.local.site_path, 'owncloud', 'backups')):
		frappe.create_folder(os.path.join(frappe.local.site_path, 'owncloud', 'backups''))


