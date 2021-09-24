#!/usr/bin/env python

import os
from posix import SCHED_FIFO
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from loader import Loader

app = App(token=os.environ["SLACK_BOT_TOKEN"])
client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

@app.event("app_mention")
def catch_event(body, say, logger):
    user_id = body['event']['user']
    user_info = client.users_info(
        user=user_id
    )
    say(f"<@{user_info['user']['name']}> OK. Please wait...")
    raw_message = body['event']['blocks'][0]['elements'][0]['elements'][1]['text']
    loaderObj = Loader(raw_message, user_info)
    response = loaderObj.get_response()
    if len(response['method']) != 0:
        if response['method'] == 'chat_postMessage':
            client.chat_postMessage(channel=body['event']['channel'], text=response['text'], username=user_info['user']['name'], attachments=response['attachments'])
        else:
            say(f"<@{user_info['user']['name']}>, something went wrong. Error: Invalid client method. Please contact bot admin.")
    elif len(response) != 0:
        say(f"<@{user_info['user']['name']}>, {response}")
    else:
        say(f"<@{user_info['user']['name']}>, I could not get any response from the backend. Please contact bot admin.")

# TO DO: put this in a separate module callable here in main runner
# Your function will only be called when the action_id matches 'select_user' AND the block_id matches 'assign_ticket'
@app.action({
    "block_id": "actionblock1",   
    "action_id": "submitbtn1"
})
def update_message(ack, body, client):
    client.replyInteractive('test message')
    #print(body)
    ack()

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()