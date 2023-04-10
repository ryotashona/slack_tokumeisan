import re
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def reactions_add(ack, respond, command, client:WebClient, channel):
    ack()

    try:
        args = command["text"].split()
        if len(args) != 2:
            raise ValueError("正しい形式で入力してください: /tokumei_stamp [スタンプしたい投稿URL] [emoji]")

        permalink, emoji = args
        match = re.match(r"https?://\S+/archives/\w+/p(\w+)", permalink)
        if not match:
            raise ValueError("無効な投稿URLです")

        timestamp = float(match.group(1)) / 1000000  # Slackのタイムスタンプ形式に変換

        client.reactions_add(channel=channel['id'], timestamp=str(timestamp), name=emoji.strip(':'))
        respond(text=f"{permalink} へ {emoji} リアクションをしました", response_type="ephemeral")
    except ValueError as e:
        respond(text=f"エラー: {e}")
    except SlackApiError as e:
        respond(text=f"エラー: 匿名リアクションの追加に失敗しました。t={timestamp} n={emoji} ({e})")
