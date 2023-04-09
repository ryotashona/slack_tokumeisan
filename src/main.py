import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import tokumei

app = App()

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
channel_id = os.environ["CHANNEL_ID"]
channel_info = client.conversations_info(channel=channel_id)
channel_name = channel_info["channel"]["name"]

@app.command("/tokumei")
def tokumei_post_handler(ack, respond, command):
    tokumei.post_message(ack, respond, command, client, channel_info["channel"])

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
