# Alekseeva Elena

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Примечание: В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве несколько раз,
# используйте один любой по вашему выбору.

import random

array = [random.randint(-100, 100) for _ in range(10)]
for i in range(len(array)):
    print(array[i], end=' ')
print()


# 1-ый (классический) вариант
mn = 0
mx = 0
for i in range(len(array)):
    if array[i] < array[mn]:
        mn = i
    elif array[i] > array[mx]:
        mx = i
print(f'Min: array[{mn+1}]={array[mn]} \nMax: array[{mx+1}]={array[mx]}')
b = array[mn]
array[mn] = array[mx]
array[mx] = b

for i in range(len(array)):
    print(array[i], end=' ')
print()


# 2-й вариант
mn = min(array)
mx = max(array)
imn = array.index(mn)
imx = array.index(mx)
print(f'Min: array[{imn + 1}]={mn} \nMax: array[{imx + 1}]={mx}')
array[imn], array[imx] = array[imx], array[imn]

for i in range(len(array)):
    print(array[i], end=' ')
print()
