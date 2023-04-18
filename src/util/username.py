import re

from slack_sdk import WebClient

# ユーザー名とIDを取得
def get_all_users(client:WebClient):
    users = []
    cursor = None

    while True:
        response = client.users_list(limit=200, cursor=cursor)

        if not response['ok']:
            raise ValueError(f"Error fetching users: {response['error']}")

        # 必要な情報（ユーザー名とID）だけを抽出
        minimal_users = [{'id': user['id'], 'name': user['name']} for user in response['members']]
        users += minimal_users

        cursor = response.get('response_metadata', {}).get('next_cursor', None)

        if not cursor:
            break

    return users

def replace_usernames_with_ids(client:WebClient, text):

    # 特殊メンション
    text = text.replace("@here", "<!here>")
    text = text.replace("@channel", "<!channel>")

    # ユーザーメンション抽出
    usernames = re.findall(r'@([\w._\-]+)(?!\w)(?<!\w@\w)', text)

    if not usernames:
        # ユーザーメンションなし
        return text
    
    # ユーザー名とIDを取得
    users = get_all_users(client)
    
    # ユーザー名をidに置換
    for username in usernames:
        user_id = next((user['id'] for user in users if user['name'] == username), None)

        if user_id:
            text = text.replace(f"@{username}", f"<@{user_id}>")

    return text

