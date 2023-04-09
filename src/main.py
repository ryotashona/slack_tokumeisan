import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import anon_post_handler as tokumei

app = App()

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
