from client import AvatarsClient, ConvertTextClient


result = AvatarsClient()


data =  result.response_json()
# status = result.response_status()
str_data = result.convert_response_list_to_str()

list_names_affiliation_avatars = [{"nome": avatar['name'], "afiliacao": avatar['affiliation'] if 'affiliation' in avatar else "Sem afiliação"} for avatar in data ]



source_lang = "en"
target_lang = "pt"
 
texto_conversor = ConvertTextClient(list= list_names_affiliation_avatars, source_lang=source_lang, target_lang=target_lang)

print(texto_conversor.translater_en_to_br())
