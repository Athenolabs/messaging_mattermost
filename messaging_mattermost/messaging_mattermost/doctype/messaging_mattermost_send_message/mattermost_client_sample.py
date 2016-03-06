# -*- coding: utf-8 -*-
import requests

import mattermost

# TODO: create button in ERPNext app.
#   TODO: Добавить вызов Python-обработчика из JS-обработчика
# TODO: create DocField with list of users from User DocType. In Python frappe.session.user
# TODO: get list of teams
# TODO: create new user

url = 'http://52.86.156.200/api/v1'
# url = 'http://192.168.99.100:32770/api/v1'
# api = mattermost.MattermostAPI(url)
# api.login('new_user', 'new_user@mail.ru', 'new_user')
team = 'exampleteam'
# team = 'myteam'
email = 'someone@nowhere.com'
# email = 'osya@mail.ru'
password = 'osyaosya'
client = mattermost.MattermostClient(url, team, email, password)

# post message in a channel
channels = client.api.get_channels()
channel = channels[1]['id']
client.channel_msg(channel, 'test message13')
#
# # get message list
# messages = client.api.get_channel_posts(channel, 0)
# message_list = [messages['posts'][m]['message'] for m in messages['posts']]
# # messages = list(client.messages())
#
# with requests.Session() as s:
#     # # Authentication of already existing user in existing group. Get token in the result
#     # url = 'http://52.86.156.200/api/v1/users/login'
#     # data = '{"name": "exampleteam", "email": "someone@nowhere.com", "password": "osyaosya"}'
#     # r = s.post(url, data=data)
#     # # token = r.headers['Token']
#     #
#     # # Send message
#     # url = 'http://52.86.156.200/api/v1/channels/twfut7rrspn4bejsk9i81k3zuc/create'
#     # data = '{"filenames":[],"message":"test message2","channel_id":"twfut7rrspn4bejsk9i81k3zuc","pending_post_id":"sbowhkfbuj8fbrx74h8nooer7h:1456821261300","user_id":"sbowhkfbuj8fbrx74h8nooer7h","create_at":1456821261300,"state":"loading"}'
#     # r = s.post(url, data=data)
#     # print r.text
#
#     # Authentication of already existing user in existing group. Get token in the result
#     url = 'http://52.86.156.200/api/v1/users/login'
#     data = '{"name": "exampleteam", "email": "someone@nowhere.com", "password": "osyaosya"}'
#     r = s.post(url, data=data)
#     # token = r.headers['Token']
#
#     # Send message
#     url = 'http://52.86.156.200/api/v1/channels/twfut7rrspn4bejsk9i81k3zuc/create'
#     data = '{"filenames":[],"message":"test message2","channel_id":"twfut7rrspn4bejsk9i81k3zuc","pending_post_id":"sbowhkfbuj8fbrx74h8nooer7h:1456821261300","user_id":"sbowhkfbuj8fbrx74h8nooer7h","create_at":1456821261300,"state":"loading"}'
#     r = s.post(url, data=data)
#     print r.text