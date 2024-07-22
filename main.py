cook_book = {}
with open('recipe.txt', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line.isdigit():
            continue
        elif line and '|' not in line:
            cook_book[line] = []
            key = line
        elif line and '|' in line:
            name, quantity, measure = line.split(" | ")
            cook_book.get(key).append(dict(ingredient_name=name, quantity=int(quantity), measure=measure))

print(cook_book)



def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                new_shop_list_item = dict(ingredient)
                new_shop_list_item['quantity'] *= person_count
                if new_shop_list_item['ingredient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))




import glob, os
def new_txt_file():
    path = 'C:\\Users\\1\\Desktop\\нетология\\ООП и айди\\Открытие и чтение файла\\Задача№3'
    pattern = '*.txt'

    glob_path = os.path.join(path, pattern)
    list_files = glob.glob(glob_path)
    all_files=[]
    if list_files:
        for file_name in list_files:
            with open(file_name,'r',encoding='utf-8') as fr:
                file=[]
                text=""
                count=0
                name_file=""
                for line in fr:
                    count+=1
                    if(count<=1):
                        name_file=os.path.basename(file_name)
                    text+=line

                file.append(str(count))
                file.append(name_file)
                file.append(text)
                all_files.append(file)
                all_files.sort()

    with open('result.txt', 'w', encoding='utf-8') as file_result:
        for my_file in all_files:
            file_result.write(f'{my_file[1]}\n{my_file[0]}\n{my_file[2]}\n')

new_txt_file()

