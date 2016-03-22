# -*- coding: utf-8 -*-
# Copyright (c) 2015, Semilimes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import frappe.email.mattermost

# TODO; Отсортировать отображаемые сообщения по времени
# TODO: investigating add path to mettermost module to PYTHONPATH. Fix $PATH variable
# TODO: integrate Mattermost user accounts with ERPNext user accounts
# TODO: Получение настроек подключения вынести в конструктор

class MattermostSingleDocType(Document):
	pass

@frappe.whitelist()
def send_message(message):
	settings = frappe.get_doc("Mattermost Settings", "Notifications")
	url = settings.url
	team = settings.team
	email = settings.email
	password = settings.password
	client = frappe.email.mattermost.MattermostClient(url, team, email, password)

	# post message in a channel
	channels = client.api.get_channels()
	channel = channels[1]['id']
	client.channel_msg(channel, message)

@frappe.whitelist()
def get_message_list():
	settings = frappe.get_doc("Mattermost Settings", "Notifications")
	url = settings.url
	team = settings.team
	email = settings.email
	password = settings.password
	client = frappe.email.mattermost.MattermostClient(url, team, email, password)

	channels = client.api.get_channels()
	channel = channels[1]['id']

	messages = client.api.get_channel_posts(channel, 0)
	message_list = [messages['posts'][m]['message'] for m in messages['posts']]
	return '\n'.join(message_list)
