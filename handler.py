import logging

import slack


class SlackAlertHandler(logging.NullHandler):
    def __init__(self, token, channel, prefix):
        super().__init__()
        self.prefix = prefix
        self.channel = channel
        self.client = slack.WebClient(token=token)

    def handle(self, record):
        """로그 발사"""
        content = self.format(record)
        self.client.chat_postMessage(channel=self.channel, text=f"[{self.prefix}] {content}")
