# Alekseeva Elena
"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.

Примечания:
* в сумму не включаем пустую строку и строку целиком;
* задача считается решённой, если в коде использована функция вычисления хеша (hash(),
sha1() или любая другая из модуля hashlib)
"""
import hashlib


def subs_in_str(string):
    if len(string) == 0 or len(string) == 1:
        return len(string)
    hash_list = []
    step = 1
    while step < len(string):
        for i in range(0, len(string), 1):
            hash_tmp = hashlib.sha1(string[i:i + step].encode('utf-8')).hexdigest()
            if hash_tmp not in hash_list:
                hash_list.append(hash_tmp)
        step += 1
    return len(hash_list)


input_str = input('Введите строку: ')
count_subst = subs_in_str(input_str)
print(f'Число подстрок в строке: {count_subst}')
