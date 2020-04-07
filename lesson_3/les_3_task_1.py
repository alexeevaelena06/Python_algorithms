# Alekseeva Elena

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

# 1-ый вариант

MAX_NUMBER = 99
MIN_DIV = 2
MAX_DIV = 9

print('Делитель    Чисел на него делится')

for div in range(MIN_DIV, MAX_DIV + 1):
    print(f'{div:>6} {MAX_NUMBER // div:>16}')

# 2-ой вариант
# a = [0] * 8
# for i in range(2, 100):
#     for j in range(2, 10):
#         if i % j == 0:
#             a[j - 2] += 1
# i = 0
# while i < len(a):
#     print(i + 2, ' - ', a[i])
#     i += 1
