import re
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from util import username

def modal_open(ack, body, client):
    # モーダルの定義
    modal = {
        "type": "modal",
        "callback_id": "tokumei_thread_modal",
        "title": {
            "type": "plain_text",
            "text": "Example Modal"
        },
        "submit": {
            "type": "plain_text",
            "text": "Submit"
        },
        "blocks": [
            {
                "type": "input",
                "block_id": "url_block",
                "label": {
                    "type": "plain_text",
                    "text": "URL"
                },
                "element": {
                    "type": "plain_text_input",
                    "action_id": "url_input"
                }
            },
            {
                "type": "input",
                "block_id": "comment_block",
                "label": {
                    "type": "plain_text",
                    "text": "Comment"
                },
                "element": {
                    "type": "plain_text_input",
                    "action_id": "comment_input",
                    "multiline": True
                }
            }
        ]
    }

    # モーダルを表示
    client.views_open(trigger_id=body["trigger_id"], view=modal)
    
    # リクエストの受信を確認
    ack()

def post_thread_message(ack, body, logger, client:WebClient, channel):
    ack()

    # try:
    permalink = body['view']['state']['values']['url_block']['url_input']['value']
    message = body['view']['state']['values']['comment_block']['comment_input']['value']

    match = re.match(r"https?://\S+/archives/\w+/p(\w+)", permalink)
    if not match:
        raise ValueError("無効な投稿URLです")

    timestamp = float(match.group(1)) / 1000000  # Slackのタイムスタンプ形式に変換

    message = username.replace_usernames_with_ids(client, message)
    client.chat_postMessage(channel=channel['id'], thread_ts=str(timestamp), text=message)
    #     respond(text=f"{permalink} へ匿名返信をしました ts={timestamp} msg={message}", response_type="ephemeral")
    # except ValueError as e:
    #     respond(text=f"エラー: {e}")
    # except SlackApiError as e:
    #     respond(text=f"エラー: 匿名返信に失敗しました。t={timestamp} ({e})")
