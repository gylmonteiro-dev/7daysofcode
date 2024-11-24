from googletrans import Translator
import json
import requests


class AvatarsClient:
    def __init__(self):
        self.base_url = "https://last-airbender-api.fly.dev/api/v1/characters"


    def response_json(self):
        response = requests.get(f"{self.base_url}")
        data = response.json()
        return data
    
    def response_status(self):
        response = requests.get(f"{self.base_url}")
        return response.status_code
    
    def convert_response_list_to_str(self):
        data = self.response_json()
        data = json.dumps(data, indent=4)
        return data


class ConvertTextClient:
    def __init__(self, list, source_lang = "", target_lang = ""):
        self.list_avatars = list
        self.source_lang = source_lang
        self.target_lang = target_lang
        

    def translater_en_to_br(self):
        translator = Translator()
        list_names_and_avatares = [{'nome': translator.translate(avatar['nome'], src=self.source_lang, dest=self.target_lang).text, 'afiliacao': translator.translate(avatar['afiliacao'], src=self.source_lang, dest=self.target_lang).text } for avatar in self.list_avatars]

        return list_names_and_avatares
