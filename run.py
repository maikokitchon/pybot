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
    loaderObj = Loader(raw_message)
    response = loaderObj.get_response()
    if len(response) != 0:
        say(f"<@{user_info['user']['name']}>, {response}")
    else:
        say(f"<@{user_info['user']['name']}>, I could not get any response from the back end. Please contact bot admin.")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()