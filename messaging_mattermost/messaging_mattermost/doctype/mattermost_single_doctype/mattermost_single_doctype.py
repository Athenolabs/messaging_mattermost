# -*- coding: utf-8 -*-
# Copyright (c) 2015, Semilimes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import frappe.email.mattermost


# TODO: Получение настроек подключения вынести в конструктор
# TODO: переделать функцию получения сообщений на messages()
# TODO: сделать получение списка сообщений при старте формы. А также polling для обновления списка сообщений

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

    users = client.get_users()
    messages = client.api.get_channel_posts(channel, 0)
    posts = sorted([(users[m['user_id']]['username'], m['create_at'], m['message']) for m in messages['posts'].values()], key=lambda x: x[1])

    return '\n'.join(map(lambda x: '%s: %s' % (x[0], x[2]), posts))
