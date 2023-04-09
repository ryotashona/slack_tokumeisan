import re
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def post_thread_message(ack, respond, command, client:WebClient, channel):
    ack()

    try:
        args = command["text"].split(' ',1)
        if len(args) != 2:
            raise ValueError("正しい形式で入力してください: /tokumei_thread [返信したい投稿URL] [コメント] ")

        permalink = args[0]
        message = args[1]
        match = re.match(r"https?://\S+/archives/\w+/p(\w+)", permalink)
        if not match:
            raise ValueError("無効な投稿URLです")

        timestamp = float(match.group(1)) / 1000000  # Slackのタイムスタンプ形式に変換

        client.chat_postMessage(channel=channel['id'], thread_ts=timestamp, text=message)
        respond(text=f"{permalink} へ匿名返信をしました ts={timestamp} msg={message}", response_type="ephemeral")
    except ValueError as e:
        respond(text=f"エラー: {e}")
    except SlackApiError as e:
        respond(text=f"エラー: 匿名返信に失敗しました。t={timestamp} ({e})")
