# Alekseeva Elena

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# Примечание:
# В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве несколько раз,
# используйте один любой по вашему выбору.

import random

a = [random.randint(-100, 100) for _ in range(10)]
for i in range(len(a)):
    print(a[i], end=' ')
print()

min_id = 0
max_id = 0
for i in range(1, len(a)):
    if a[i] < a[min_id]:
        min_id = i
    elif a[i] > a[max_id]:
        max_id = i
print(f"Min: {a[min_id]}, \nMax: {a[max_id]}")

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
for i in range(min_id + 1, max_id):
    summa += a[i]
print(f"Сумма элементов = {summa} между Min: {a[min_id]} и Max: {a[max_id]} элементами массива")
