import requests
import json
import configparser
from config import token


class TelegramBot:
    def __init__(self):
        # self.token = self.read_token_from_config(token)
        self.base = "https://api.telegram.org/bot{}/".format(token)

    def _post(self, endpoint, new_solution_document=None, new_message=None, chat_id=None, reply_to_message_id=None):
        response = None
        if new_solution_document:
            url = self.base+endpoint+"?chat_id={}&reply_to_message_id={}&caption={}".format(
                new_solution_document.chat_id,
                new_solution_document.reply_to_message_id,
                new_solution_document.caption
            )
            response = requests.post(url, files={'document': new_solution_document.file_descriptor})
        elif new_message:
            url = self.base + endpoint + "?chat_id={}&text={}&reply_to_message_id={}".format(
                chat_id,
                new_message,
                reply_to_message_id
            )
            response = requests.get(url)

        return response

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url+"&offset={}".format(offset+1)
            print(url)
            url_response = requests.get(url)
            return json.loads(url_response.content)

    def send_document(self, new_solution_document, endpoint='sendDocument'):
        url_response = self._post(endpoint=endpoint, new_solution_document=new_solution_document)
        return url_response
    
    def send_error_message(self, chat_id, reply_to_msg, text):
        url_response = self._post(endpoint='sendMessage', new_message=text,
                                  chat_id=chat_id, reply_to_message_id=reply_to_msg)
        return url_response

    def send_text_message(self, chat_id, text):
        url_response = self._post(endpoint='sendMessage', new_message=text, chat_id=chat_id)
        return url_response

    @staticmethod
    def read_token_from_config(config):
        parser = configparser.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')
