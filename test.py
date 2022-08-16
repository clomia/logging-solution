import ssl
import slack

ssl._create_default_https_context = ssl._create_unverified_context

slack_token = "xoxb-3019904477665-3737651200213-vdnNuYZ4vlGWl8qui81tZYMN"  # 발급받은 Token 값
client = slack.WebClient(token=slack_token)
client.chat_postMessage(channel="#alert", text="안녕하세요 저는 알럴트라고 해요!")
