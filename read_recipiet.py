def parse_recipes(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        if lines[i].strip():  # Проверяем, что строка не пустая
            recipe_name = lines[i].strip()
            cook_book[recipe_name] = []
            ingredient_count = int(lines[i + 1].strip())
            for j in range(ingredient_count):
                ingredient_info = lines[i + 2 + j].strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                cook_book[recipe_name].append(ingredient)
            i += ingredient_count + 2
        i += 1

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    # функция для расчёта количества необходимых продуктов в зависимости от количества персон
    goods_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name not in goods_list:
                    goods_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    goods_list[ingredient_name]['quantity'] += quantity
    return goods_list


# Пример использования
file_path = 'recipes.txt'
cook_book = parse_recipes(file_path)
print(cook_book)

print(get_shop_list_by_dishes(['Борщ', 'Оливье'], 3))
