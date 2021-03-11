import os

file_path = os.path.join(os.getcwd(), 'cook_book.txt')


def cook_book_func(file_path):
    cook_book = {}
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            while True:
                ingredient = f.readline().rstrip()
                cook_book[ingredient] = []
                cnt_ingredients = int(f.readline().rstrip())
                for j in range(cnt_ingredients):
                    lst = f.readline().rstrip().split(' | ')
                    cook_book[ingredient].append({'ingredient_name': lst[0], 'quantity': int(lst[1]), 'measure': lst[2]})
                print(f.readline().rstrip(), end='')
        except ValueError:
            del cook_book['']
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dict = {}
    result = 0
    for j in dishes:
        for i in cook_book_func(file_path)[j]:
            if i['ingredient_name'] not in ingredients_dict:
                ingredients_dict[i['ingredient_name']] = {'measure': i['measure'],
                                                          'quantity': i['quantity']*person_count}
            else:
                result = ingredients_dict[i['ingredient_name']]['quantity'] + i['quantity']*person_count
                ingredients_dict[i['ingredient_name']] = ({'measure': i['measure'],
                                                          'quantity': result})
    return ingredients_dict


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

