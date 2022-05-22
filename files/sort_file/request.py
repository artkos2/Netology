import requests
from datetime import datetime, time, timedelta
api_url_hero = 'https://www.superheroapi.com/api/'
api_token_nero = '2619421814940190'
api_url_ya = 'https://cloud-api.yandex.net/v1/disk/resources'
api_url_stack = 'https://api.stackexchange.com/2.3/'
api_ya_token = 'AQAAAAABK47YAADLW_X6czWxmUj3uZSHCEbWLV4'

superheros = ['Hulk', 'Captain America', 'Thanos', 'Batman']

def get_id(superhero_list):
    hero_ids = []
    for hero in superhero_list:
        data = requests.get(api_url_hero+api_token_nero+'/search/'+hero)
        hero_ids.append(data.json()['results'][0]['id'])
    return hero_ids

def get_intelligence(hero_ids):
    hero_intelligence = {}
    for id in hero_ids:
        data = requests.get(api_url_hero+api_token_nero+'/'+id)
        hero_intelligence[data.json()['powerstats']['intelligence']] = data.json()['name']
        sorted_dict_files = sorted(hero_intelligence.items())
    print(f'Самый умный супергерой - {sorted_dict_files[0][1]}')

class YaUploader:
    def __init__(self, api_ya_token: str):
        self.token = api_ya_token
    def upload(self, path_ya, path_to_file):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {api_ya_token}'}
        upload_url = requests.get(f'{api_url_ya}/upload?path={path_ya}&overwrite=true', headers=headers).json()
        with open(path_to_file, 'rb') as f:
            requests.put(upload_url['href'], files={'file':f})
            print(f'Файл {path_to_file} успешно загружен')

        # print(res)

def get_id_question(number_days = 2):
    questions_ids = []
    todate = int(datetime.combine(datetime.now(), time.max).timestamp())
    fromdate = int(datetime.combine(datetime.now() - timedelta(days=number_days), time.min).timestamp())
    data = requests.get(api_url_stack+'answers?fromdate='+str(fromdate)+'&todate='+str(todate)+'&order=desc&sort=activity&site=stackoverflow')
    for item in data.json()['items']:
        questions_ids.append(str(item['answer_id']))
    return questions_ids

def get_title_question(questions_ids, search_tag = 'python'):
    count = 0
    for id in questions_ids:
        data = requests.get(api_url_stack+'answers/'+id+'/questions?order=desc&sort=activity&site=stackoverflow')
        if search_tag in data.json()['items'][0]['tags']:
            count += 1
            print(data.json()['items'][0]['title'])
    print(f'За последние 2 дня вопросов с тэгом Python - {count}')


if __name__ == '__main__':
    get_intelligence(get_id(superheros))
    ya_upload_file = YaUploader(api_ya_token)
    result = ya_upload_file.upload('Netology/testYa.txt','files/testYa.txt')
    get_title_question(get_id_question())