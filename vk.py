import requests
from pprint import pprint
import time


with open('files/tokenVK.txt', 'r') as file_object:
    token = file_object.read().strip()

# users_id_list = ['3223792', 'kotenok_gav_22']
#  alex_nemchinoff & 431431 & martart
mutual_frends_ids = []
mutual_frends_names = []

class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        # self.id = id
        self.params = {
            'access_token': token,
            'v': version    
        }
    
    def get_frends(self, user_id=None):
        frends_url = self.url + 'friends.get'
        if user_id.isdigit():
            user_id = user_id
        else:
            user_id = VK.get_id(user_id)
        frends_params = {
            'user_id': user_id
        }
        res = requests.get(frends_url, params={**self.params, **frends_params}).json()
        # pprint(res['response']['items'])
        return res['response']['items']

    def get_name(self, id):
        name_url = self.url + 'users.get'
        name_params = {
            'user_ids': id
        }
        # print(str(ids))
        res = requests.get(name_url, params={**self.params, **name_params}).json()
        # pprint(res)
        # print(res['response'][0]['first_name'] + ' ' + res['response'][0]['last_name'])
        return res['response'][0]['first_name'] + ' ' + res['response'][0]['last_name']
    def get_id(self, screen_name):
        name_url = self.url + 'users.get'
        name_params = {
            'user_ids': screen_name
        }
        # print(str(ids))
        res = requests.get(name_url, params={**self.params, **name_params}).json()
        # pprint(res)
        # print(res['response'][0]['first_name'] + ' ' + res['response'][0]['last_name'])
        return res['response'][0]['id']
    def get_name_for_ids(self, ids):
        count = 0
        for id in ids:
            print(VK.get_name(id))
            time.sleep(0.33)
            # print(mutual_frends_names)
            count +=1
        print(f'Всего общих друзей - {count}')

def mutual_frends(users_id_list):
    temp_list = []
    for number in range(0, len(users_id_list)):  
        id = VK.get_frends(users_id_list[number])
        temp_list.extend(id)
    for id in temp_list:
        if temp_list.count(id) == len(users_id_list) and id not in mutual_frends_ids:
            mutual_frends_ids.append(id)
    if len(mutual_frends_ids) == 0:
        print('Общих друзей не найдено')
    else:
        VK.get_name_for_ids(mutual_frends_ids)
        # print(mutual_frends_ids)

if __name__ == '__main__':
    str = input('Введите id пользователей (разделитель &)')
    users_id_list = str.replace(" ", "").split('&')
    VK = VkUser(token, '5.131')
    mutual_frends(users_id_list)
    # list = ['11', '113', '443']
    # print(list.count('11'))
    
