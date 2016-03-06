# -*- coding: utf-8 -*-
# Copyright (c) 2015, Semilimes and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import sys
sys.path.append(r"/home/vagrant/bench/apps/messaging_mattermost/messaging_mattermost/messaging_mattermost")
import mattermost


class MessagingMattermostGetMessageList(Document):
    pass


@frappe.whitelist()
def get_message_list():
    url = 'http://52.86.156.200/api/v1'
    team = 'exampleteam'
    email = 'someone@nowhere.com'
    password = 'osyaosya'
    client = mattermost.MattermostClient(url, team, email, password)

    channels = client.api.get_channels()
    channel = channels[1]['id']

    messages = client.api.get_channel_posts(channel, 0)
    message_list = [messages['posts'][m]['message'] for m in messages['posts']]
    return '\n'.join(message_list)
