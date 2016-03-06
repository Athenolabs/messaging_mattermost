# -*- coding: utf-8 -*-
# Copyright (c) 2015, Semilimes and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import sys
sys.path.append(r"/home/vagrant/bench/apps/messaging_mattermost/messaging_mattermost/messaging_mattermost")
import mattermost


# TODO: investigating add path to mettermost module to PYTHONPATH. Fix $PATH variable
# TODO: integrate Mattermost user accounts with ERPNext user accounts
# TODO; Отсортировать отображаемые сообщения по времени

# noinspection SpellCheckingInspection
class MessagingMattermostSendMessage(Document):
    pass


@frappe.whitelist()
def send_message(message):
    url = 'http://52.86.156.200/api/v1'
    team = 'exampleteam'
    email = 'someone@nowhere.com'
    password = 'osyaosya'
    client = mattermost.MattermostClient(url, team, email, password)

    # post message in a channel
    channels = client.api.get_channels()
    channel = channels[1]['id']
    client.channel_msg(channel, message)
