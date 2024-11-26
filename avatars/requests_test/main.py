from .client import AvatarsClient, ConvertTextClient

# status = result.response_status()
# str_data = result.convert_response_list_to_str()

def list_avatares():
    result = AvatarsClient()
    data =  result.response_json()
    list_names_affiliation_avatars = [{"nome": avatar['name'], "afiliacao": avatar['affiliation'] if 'affiliation' in avatar else "Sem afiliação"} for avatar in data ]
    return list_names_affiliation_avatars


def translate_avatars():
    avatares = list_avatares()
    source_lang = "en"
    target_lang = "pt"
    texto_conversor = ConvertTextClient(list= avatares, source_lang=source_lang, target_lang=target_lang)
    data_translate = texto_conversor.translater_en_to_br()
    return data_translate

