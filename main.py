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




with open('1.txt', 'r', encoding='utf-8') as file_1:
    line_1 = {}
    count_1 = 0
    for line in file_1.readlines():
        count_1 += 1
        line_1['1.txt'] = count_1
with open('1.txt', 'r', encoding='utf-8') as file_1:
    text_1 = file_1.read()

with open('2.txt', 'r', encoding='utf-8') as file_2:
    line_2 = {}
    count_2 = 0
    for line in file_2.readlines():
        count_2 += 1
        line_2['2.txt'] = count_2
with open('2.txt', 'r', encoding='utf-8') as file_2:
    text_2 = file_2.read()


with open('result.txt', 'w', encoding='utf-8') as file_result:
    join = sorted(list(line_ 1.items()) + list(line_2.items()), key=lambda x: x[1])
    file_result.write(f'{join[0][0]}\n {join[0][1]}\n {text_2}\n {join[1][0]}\n {join[1][1]}\n {text_1}\n')
print(file_result)