from slack_sdk import WebClient

def post_message(ack, respond, command, client:WebClient, channel):
    ack()
    client.chat_postMessage(channel=channel['id'], text=command['text'])
    respond(text=f"<#{channel['id']}|{channel['name']}> へ匿名投稿しました", response_type="ephemeral")
