## Messaging Mattermost

Mattermost client for Frappe

### Installation
 - switch to mattermost branch in bench & frappe repository
 - bench --site erpnext.dev reinstall # to create "Matttermost Settings" doctype
 - bench get-app messaging_mattermost https://github.com/semilimes/messaging_mattermost.git
 - bench --site erpnext.dev install-app messaging_mattermost
 - Set up Mattermost Connection settings:
   - Mattermost Account Name: should be Notifications
   - Url: http://52.86.156.200/api/v1
   - Team: exampleteam
   - Email: email for your user
   - Password: password for your user

### License

MIT

