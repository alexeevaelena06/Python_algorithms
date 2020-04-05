# Alekseeva Elena

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Примечание:
# В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве несколько раз,
# используйте один любой по вашему выбору.

from random import random

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random() * 200)
        b.append(n)
        print(f'  {n}', end='')
    a.append(b)
    print()

mx = -1
for j in range(M):
    mn = 200
    for i in range(N):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)
