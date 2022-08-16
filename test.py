import ssl
import slack

ssl._create_default_https_context = ssl._create_unverified_context

slack_token = "복사한 토큰을 이곳에 붙여넣기"  # 발급받은 Token 값
client = slack.WebClient(token=slack_token)
client.chat_postMessage(channel="#alert", text="안녕하세요 저는 알럴트라고 해요!")
