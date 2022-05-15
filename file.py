from pprint import pprint
from itertools import count
import os

cook_book = {}
def make_cook_book(file_path):
    count = 0
    name = ''
    with open(file_path) as file:
        for line in file:
            if len(cook_book) == count:
                cook_book[line.rstrip('\n')] = []
                name = line.rstrip('\n')
            else:
                number = int(line)
                ingredients = []
                count += 1
                for number in range(number):
                    lines = {'ingredient_name': '', 'quantity': '', 'measure': ''}
                    data = file.readline().strip().split(' | ')
                    lines['ingredient_name'] = data[0]
                    lines['quantity'] = data[1]
                    lines['measure'] = data[2]
                    ingredients.append(lines)
                cook_book[name] = ingredients
                file.readline()
    pprint(cook_book) 

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dishe in dishes:
        for line in cook_book[dishe]:
            if line['ingredient_name'] in shop_list:
                shop_list[line['ingredient_name']]['quantity'] += shop_list[line['ingredient_name']]['quantity']
            else:
                ing = {'measure': line['measure'], 'quantity':  int(line['quantity']) * person_count}
                shop_list[line['ingredient_name']] = ing
    pprint(shop_list)


def sort_files(files_dir, final_file_name = 'final_file.txt'):
    dict_files = {}
    files_list = os.listdir(path=files_dir)
    for file_name in files_list:
        with open(os.path.join(files_dir,file_name)) as file:
            dict_files[len(file.readlines())] = file_name
            sorted_dict_files = dict(sorted(dict_files.items()))
    for length, file_name in sorted_dict_files.items():
        with open(os.path.join(files_dir,final_file_name), 'a') as final_file:
            final_file.write(f'{file_name}\n')
            final_file.write(f'{length}\n')
            with open(os.path.join(files_dir,file_name)) as file:
                data = file.readlines()
                data = [line.strip() for line in data]
                final_file.write('\n'.join(data) + '\n')


make_cook_book('files/recipes.txt')
get_shop_list_by_dishes(['Утка по-пекински', 'Омлет', 'Омлет'], 4)
sort_files('files/sort_file')