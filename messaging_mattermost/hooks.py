# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "messaging_mattermost"
app_title = "Messaging Mattermost"
app_publisher = "Semilimes"
app_description = "Mattermost client for Frappe"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "valeriy.osipov@semilimes.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/messaging_mattermost/css/messaging_mattermost.css"
# app_include_js = "/assets/messaging_mattermost/js/messaging_mattermost.js"

# include js, css files in header of web template
# web_include_css = "/assets/messaging_mattermost/css/messaging_mattermost.css"
# web_include_js = "/assets/messaging_mattermost/js/messaging_mattermost.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "messaging_mattermost.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "messaging_mattermost.install.before_install"
# after_install = "messaging_mattermost.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "messaging_mattermost.notifications.get_notification_config"

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
# 		"messaging_mattermost.tasks.all"
# 	],
# 	"daily": [
# 		"messaging_mattermost.tasks.daily"
# 	],
# 	"hourly": [
# 		"messaging_mattermost.tasks.hourly"
# 	],
# 	"weekly": [
# 		"messaging_mattermost.tasks.weekly"
# 	]
# 	"monthly": [
# 		"messaging_mattermost.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "messaging_mattermost.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "messaging_mattermost.event.get_events"
# }

