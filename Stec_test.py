import os

#
now_dir = 'чеки_по_папкам'
os.mkdir(now_dir)

# читаем файл "чеки.txt" в список lines. Используем -sig, дабы избавиться от '/ufeff'
with open('чеки.txt', encoding="utf-8-sig") as file:
    lines = file.readlines()
print(lines)

month_dict = {}

#
for idx in lines:
    word = idx.split("_")
    if word:
        key = word[1].split(".")[0]
        value = idx.replace("\n", "")
        if key in month_dict:
            month_dict[key] += value
        else:
            month_dict[key] = value
print(month_dict)

#
for key, value in month_dict.items():
    month = os.path.join(now_dir, key)
    os.mkdir(month)

    pdf_split = value.split('.pdf')
    pdf_split.pop()
    for i in pdf_split:
        with open(os.path.join(month, f'{i}.pdf'), 'w') as new_file:
            new_file.write(value)