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
        value = idx.replace("\n", "")
        if key in month_dict:
            month_dict[key] += value
        else:
            month_dict[key] = value

# находим месяц, в котором есть все оплаты, исходя из условия
long_value = max(month_dict.values(), key=len)
long_value = long_value.split('.pdf')
long_value.pop()

now_dir = 'чеки_по_папкам'
os.mkdir(now_dir)

#режем значение по пдф, и добавляем расширение .pdf уже во время записи
for key, value in month_dict.items():
    month = os.path.join(now_dir, key)
    os.mkdir(month)

    pdf_split = value.split('.pdf')
    pdf_split.pop()

    # делим самый длинный месяц, на название услуг
    longe = []
    for i in range(len(long_value)):
        longe.append(long_value[i].split('_')[0])
    # делим месяц из цикла, на название услуг
    few = []
    for j in range(len(pdf_split)):
        few.append(pdf_split[j].split('_')[0])
    # записываем отсутствующие элемнеты/оплаты
    missing_elements = [element for element in longe if (element in longe) and (element not in few)]
    with open(os.path.join(month, (key + '.txt')), 'w') as file:
        file.write(f'не оплачены:\n{key}:\n')
        for element in missing_elements:
            file.write(element + '\n')

    for i in pdf_split:
        with open(os.path.join(month, f'{i}.pdf'), 'w') as new_file:
            new_file.write(value)