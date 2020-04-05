# Alekseeva Elena

# 4. Определить, какое число в массиве встречается чаще всего.

# Примечание:
# В задачах 3, 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве несколько раз,
# используйте один любой по вашему выбору.

# В программах ниже ищется только первое самое встречаемое число.
# Если есть другое число, которое встречается с такой же частотой как первое, то оно не определяется.


import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)


num = array[0]
max_frq = 1
for i in range(len(array) - 1):
    frq = 1
    for k in range(i + 1, len(array)):
        if array[i] == array[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array[i]

if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')
