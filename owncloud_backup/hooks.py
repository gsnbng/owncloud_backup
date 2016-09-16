# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "owncloud_backup"
app_title = "Owncloud Backup"
app_publisher = "gsn"
app_description = "App for Owncloud data backup"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sheshanarayanag@gmail.com"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/owncloud_backup/css/owncloud_backup.css"
# app_include_js = "/assets/owncloud_backup/js/owncloud_backup.js"

# include js, css files in header of web template
# web_include_css = "/assets/owncloud_backup/css/owncloud_backup.css"
# web_include_js = "/assets/owncloud_backup/js/owncloud_backup.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "owncloud_backup.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "owncloud_backup.install.before_install"
# after_install = "owncloud_backup.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "owncloud_backup.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"owncloud_backup.tasks.all"
# 	],
# 	"daily": [
# 		"owncloud_backup.tasks.daily"
# 	],
# 	"hourly": [
# 		"owncloud_backup.tasks.hourly"
# 	],
# 	"weekly": [
# 		"owncloud_backup.tasks.weekly"
# 	]
# 	"monthly": [
# 		"owncloud_backup.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "owncloud_backup.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "owncloud_backup.event.get_events"
# }

