from slack_sdk import WebClient

from util import username

def post_message(ack, respond, command, client:WebClient, channel):
    ack()
    text = username.replace_usernames_with_ids(client, command['text'])
    client.chat_postMessage(channel=channel['id'], text=text)
    respond(text=f"<#{channel['id']}|{channel['name']}> へ匿名投稿しました", response_type="ephemeral")
