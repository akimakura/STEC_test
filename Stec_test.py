# читаем файл "чеки.txt" в список lines. Используем -sig, дабы избавиться от '/ufeff'
with open('чеки.txt', encoding="utf-8-sig") as file:
    lines = file.readlines()

month_dict = {}

# распределяем наш список в словарь, где месяц будет ключом
for idx in lines:
    word = idx.split("_")
    if word:
        key = word[1].split(".")[0]
        value = idx.split('_')[0]
        if key in month_dict:
            month_dict[key].add(value)
        else:
            month_dict[key] = set([value])

# находим полный список платежей
full_value = max(month_dict.values(), key=len)

with open('чеки_по_папкам.txt', 'w') as new_file:
    for key, value in month_dict.items():
        for i in value:
            new_file.write(f'{key}/{i}_{key}.pdf\n')

    # находим отсутствующие элементы(платежи) и записываем их в текстовик, второе множество это значение словаря
    new_file.write(f'\nне оплачены:\n')
    for key, value in month_dict.items():
        element = full_value.difference(value)
        new_file.write(f'{key}:\n')
        if element:
            for check in element:
                new_file.write(check + '\n')
        else:
            new_file.write('-\n')