''' Script can be used to move multiple JIRA tickets 
    to 'Done'. 
    
    Add all the tickets you wish to close as a list
    of strings to the 'ticket_list' variable.

'''

import sys
import os
from jira import JIRA

try:
    server = os.environ['SERVER']
except:
    print('You need to set environment variables for the JIRA server')
    print('Use command in CMD:')
    print('set SERVER=<your server name>')
    sys.exit()
try:
    access_token = os.environ['TOKEN']
except:
    print('You need to set environment variables for your')
    print('Personal Access Token')
    print('Use command in CMD:')
    print('set TOKEN=<your personal access token>')
    sys.exit()
    
options = {
 'server' : server,
 'headers' : {
     'Authorization' : f'Bearer: {access_token}'
                } 
}

jira = JIRA(options)
ticket_list = [] #fill list with tickets to be closed
for ticket in ticket_list:
    try:
        issue = jira.issue(ticket)
    except:
        print(ticket, 'not found.')
        continue
    try:
        jira.transition_issue(issue, '21')
        print(ticket, 'moved to done.')
    except:
        print('Unable to move', ticket, 'to done.')
        continue

print('All possible lists moved to done.')
