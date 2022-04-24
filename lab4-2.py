import re
import hashlib
from datetime import datetime


def my_hash_fun(value):
    temp = hashlib.sha512(value).hexdigest()
    return temp[:N]


N = int(input('Введите длину хэша. Доступные значения: 1..255\n'))
start_time = datetime.now()

hash_table = {}

data_from_file = open('text4-2.txt')
for line in data_from_file:
    for dirty_word in line.split(" "):
        word = re.findall(r'[a-zA-Z\dа-яА-Я]+', dirty_word)
        if len(word) == 0:
            continue
        word = word[0]
        # print(word)
        hash_value = my_hash_fun(word.encode())
        if hash_table.get(hash_value) is not None:
            if word not in hash_table.get(hash_value):
                hash_table[hash_value].append(word)
        else:
            hash_table[hash_value] = [word]
print(hash_table.items())
print('Обработка заняла: ', datetime.now() - start_time)

# while True:
#     finding_word = input()
#     start_time = datetime.now()
#     temp_list = hash_table.get(
#         my_hash_fun(
#             finding_word.encode()
#         )
#     )
#     if finding_word in temp_list:
#         print(temp_list)
#     else:
#         print("Net takogo ;(")
#     print(datetime.now() - start_time)

letter = input('Введите букву\n')
start_time = datetime.now()
for key in hash_table:
    for word in hash_table[key]:
        if word[:1] == letter:
            hash_table[key].remove(word)
print(hash_table.items())
print(datetime.now() - start_time)

