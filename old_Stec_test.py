import os

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

# создаем папку, куда всё будет записываться
SOUCE_FILENAME = 'чеки_по_папкам'
os.mkdir(SOUCE_FILENAME)

for key, value in month_dict.items():
    month = os.path.join(SOUCE_FILENAME, key)
    os.mkdir(month)

    # находим отсутствующие элементы(платежи) и записываем их в текстовик, второе множество это значение словаря
    element = full_value.difference(value)
    with open(os.path.join(month, (key + '.txt')), 'w') as file:
        file.write(f'не оплачены:\n{key}:\n')
        for schet in element:
            file.write(schet + '\n')

    # записываем наши файлы в папку
    for i in value:
       with open(os.path.join(month, f'{i}.pdf'), 'w') as new_file:
           new_file.write(f'{i}.pdf')