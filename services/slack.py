from config import Config
from slack_sdk import WebClient
import json

class Slack:
    __client = ""

    def __init__(self):
        self.__client = WebClient(token=Config.TOKEN,timeout=120000)

    def send_message(self,emoji,message,value): 
        intro_msg  = json.dumps([
            {
            "text": emoji+" "+message,
            "color": "good",
            "fields": [
                {
                "title": "Deploy",
                "value": value
                }
            ]
            }
        ])

        response = self.__client.chat_postMessage(
            channel=Config.CHANNEL_NAME,
            username=Config.CHANNEL_NAME,
            # text=emoji+" "+message,
            color="good",
            attachments=intro_msg, 
            as_user=True
        )
