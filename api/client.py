import os
import json
import requests

class InfobipClient:
    def __init__(self) -> None:
        credentials = os.environ.get("INFOBIP_API_KEY")
        self.client = requests.Session()
        self.client.headers.update({
            'Authorization': f'App {credentials}',
            'Content-Type': 'application/json',
        })
        self.base_url = os.environ.get("BASE_URL")
        self.sender_number = os.environ.get("SENDER_NUMBER")
    
    def send_text_message(self, receive_number, last_message):
        endpoint = '/whatsapp/1/message/text'

        data = {
            "from": self.sender_number,
            "to": receive_number,
            "content": {
                "text": last_message
            }
        }

        url = f"{self.base_url}{endpoint}"
        timeout = 120
        self.client.post(url, data=json.dumps(data), timeout=timeout)
    
    def send_initial_template(self, receive_number):
        endpoint = '/whatsapp/1/message/template'
        data = {
            "messages": [
                {
                    "from": self.sender_number,
                    "to": receive_number,
                    "content": {
                        "templateName": "test_whatsapp_template_en",
                        "templateData": {
                            "body": {
                                "placeholders": ["Wesley"]
                            }
                        },
                        "language": "en"
                    }
                }
            ]
        }

        url = f"{self.base_url}{endpoint}"
        timeout = 120
        self.client.post(url, data=json.dumps(data), timeout=timeout)

        
        
    
