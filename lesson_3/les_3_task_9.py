# Alekseeva Elena

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
# Примечание:
# В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве несколько раз,
# используйте один любой по вашему выбору.

import random

# 1-ой вариант

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random.random() * 200)
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


# 2-ой вариант

SIZE = 5
matrix = [[random.randint(0, 100) for _ in range(SIZE)] for _ in range(SIZE)]

for line in matrix:
    print(*line, sep="\t")

max_=matrix[0][0]
for j in range(SIZE):
    min_ = matrix[0][j]
    for i in range(SIZE):
        if matrix[i][j] < min_:
            min_ = matrix[i][j]
    if min_ > max_:
        max_ = min_
print(f"Max in min = {max_}")


