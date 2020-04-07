# Alekseeva Elena

# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
# первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы
# проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

import cProfile

MAX_NUMBER = 99
MIN_DIV = 2
MAX_DIV = 9


def div_count(max_number):
    div_dict = dict()

    for div in range(MIN_DIV, MAX_DIV + 1):
        div_dict[div] = max_number // div

    return div_dict

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.div_count(99)"
# "les_4_task_1.div_count(99)"
# 100 loops, best of 5: 1.08 usec per loop
# "les_4_task_1.div_count(999)"
# 100 loops, best of 5: 1.1 usec per loop
# "les_4_task_1.div_count(9999)"
# 100 loops, best of 5: 1.16 usec per loop
# "les_4_task_1.div_count(99999)"
# 100 loops, best of 5: 1.18 usec per loop
# Алгоритм работает приблизительно за O(1). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивалось незначительно. При увеличении количества входных элементов в 1000 раз время
#  увеличилось всего на 9,5%

# cProfile.run('div_count(9999)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:22(div_count)  99
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:22(div_count) 999
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:22(div_count)  9999
# Алгоритм работает быстро, в оптимизации не нуждается.


def div_count_dict(max_number):
    div_dict = dict()

    for div in range(MIN_DIV, MAX_DIV + 1):
        div_dict[div] = 0

        for num in range(2, max_number + 1):

            if num % div == 0:
                div_dict[div] += 1

    return div_dict

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.div_count_dict(99)"
# "les_4_task_1.div_count_dict(99)"
# 100 loops, best of 5: 87.7 usec per loop
# "les_4_task_1.div_count_dict(999)"
# 100 loops, best of 5: 606 usec per loop
# "les_4_task_1.div_count_dict(9999)"
# 100 loops, best of 5: 6.66 msec per loop
# "les_4_task_1.div_count_dict(99999)"
# 100 loops, best of 5: 73.5 msec per loop
# Алгоритм работает приблизительно за O(n). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивается приблизительно в 10 раз.
# И даже на самом маленьком размере входных данных алгоритм работает значительно медленнее, чем div_count()

# cProfile.run('div_count_dict(99999)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:50(div_count_dict)   99
# 1    0.001    0.001    0.001    0.001 les_4_task_1.py:50(div_count_dict) 999
# 1    0.006    0.006    0.006    0.006 les_4_task_1.py:50(div_count_dict) 9999
# 1    0.066    0.066    0.066    0.066 les_4_task_1.py:50(div_count_dict) 99999
# Рекурсий в алгоритме нет, время выполнения нарастает линейно.


def div_count_xxxx(max_number):
    div_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for num in range(2, max_number + 1):

        if num % 2 == 0:
            div_dict[2] += 1

        if num % 3 == 0:
            div_dict[3] += 1

        if num % 4 == 0:
            div_dict[4] += 1

        if num % 5 == 0:
            div_dict[5] += 1

        if num % 6 == 0:
            div_dict[6] += 1

        if num % 7 == 0:
            div_dict[7] += 1

        if num % 8 == 0:
            div_dict[8] += 1

        if num % 9 == 0:
            div_dict[9] += 1

    return div_dict

# python -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.div_count_xxxx(99)"
# "les_4_task_1.div_count_xxxx(99)"
# 100 loops, best of 5: 49.4 usec per loop
# "les_4_task_1.div_count_xxxx(999)"
# 100 loops, best of 5: 527 usec per loop
# "les_4_task_1.div_count_xxxx(9999)"
# 100 loops, best of 5: 5.51 msec per loop
# "les_4_task_1.div_count_xxxx(99999)"
# 100 loops, best of 5: 55.2 msec per loop
# Алгоритм работает приблизительно за O(n). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивается приблизительно в 10 раз.
# И даже на самом маленьком размере входных данных алгоритм работает значительно медленнее, чем div_count(),
# при этом этот алгоритм чуть быстрее, чем div_count_dict()

# cProfile.run('div_count_xxxx(99)')
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:84(div_count_xxxx)   99
# 1    0.001    0.001    0.001    0.001 les_4_task_1.py:84(div_count_xxxx) 999
# 1    0.008    0.008    0.008    0.008 les_4_task_1.py:84(div_count_xxxx) 9999
# 1    0.079    0.079    0.079    0.079 les_4_task_1.py:84(div_count_xxxx) 99999
# Рекурсий в алгоритме нет, время выполнения нарастает линейно.


# ВЫВОД:
# Алгоритм, использованный в функции div_count(), является самым оптимальным и быстрым.
# Так как он выполняется практически за константное время, несильно завися от размера входных данных.


# MAX_NUMBER = 99
#
# print(div_count(MAX_NUMBER))
# print(div_count_dict(MAX_NUMBER))
# print(div_count_xxxx(MAX_NUMBER))
