# Alekseeva Elena

# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2
# Примечание по профилированию кода: для получения достоверных результатов при замере времени необходимо
# исключить/заменить функции print() и input()
# в анализируемом коде. С ними вы будете замерять время вывода данных в терминал и время,
# потраченное пользователем, на ввод данных,
# а не быстродействие самого алгоритма.

# Тестовая функция проверяет до 1229-го простого числа.

import cProfile


def test(num, n=10000):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(f'Количество простых чисел в диапазоне до {n}: {len(res)}')

    assert num < len(res)
    return res[num - 1]


def eratosthenes_sieve(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:

        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):

            for num in prime:

                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break

# python -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.eratosthenes_sieve(10)"
# "les_4_task_2.eratosthenes_sieve(10)"
# 100 loops, best of 5: 14.1 usec per loop
# "les_4_task_2.eratosthenes_sieve(100)"
# 100 loops, best of 5: 296 usec per loop
# "les_4_task_2.eratosthenes_sieve(1000)"
# 100 loops, best of 5: 24.5 msec per loop
# Предположительно, алгоритм сложности O(n**2). Увеличение количества чисел в 10 раз
# увеличивает время выполнения приблизительно в 100 раз

# cProfile.run('eratosthenes_sieve(1000)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:48(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:53(<listcomp>)
# cProfile.run('eratosthenes_sieve(100)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:48(eratosthenes_sieve)
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:53(<listcomp>)
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:75(<listcomp>)
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:78(<listcomp>)
# cProfile.run('eratosthenes_sieve(1000)')
#  1    0.025    0.025    0.026    0.026 les_4_task_2.py:48(eratosthenes_sieve)
#  1    0.000    0.000    0.000    0.000 les_4_task_2.py:53(<listcomp>)
#  2    0.000    0.000    0.000    0.000 les_4_task_2.py:75(<listcomp>)
#  2    0.000    0.000    0.000    0.000 les_4_task_2.py:78(<listcomp>)
# Время выполнения нарастает. Рекурсий нет.


def search_prime(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number

# python -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.search_prime(10)"
# "les_4_task_2.search_prime(10)"
# 100 loops, best of 5: 4.73 usec per loop
# "les_4_task_2.search_prime(100)"
# 100 loops, best of 5: 290 usec per loop
# "les_4_task_2.search_prime(1000)"
# 100 loops, best of 5: 30.9 msec per loop
# Сложность близка к O(n**2)
# Скорость работы обоих алгоритмов на данных объемах данных практически одинакова.

# cProfile.run('search_prime(1000)')
# 1    0.000    0.000    0.000    0.000 les_4_task_2.py:114(search_prime) 10
# 1    0.001    0.001    0.001    0.001 les_4_task_2.py:114(search_prime) 100
# 1    0.029    0.029    0.029    0.029 les_4_task_2.py:114(search_prime) 1000
# Время выполнения нарастает. Рекурсий нет.


# ВЫВОД:
# Сложность алгоритмов и время их работы приблизительно одинаковые.


n = 521

# if eratosthenes_sieve(n) == test(n):
#     print(f'{n}-ое простое число {eratosthenes_sieve(n)}')
#     print('OK')
# else:
#     print('Ошибка')
#
# if search_prime(n) == test(n):
#     print(f'{n}-ое простое число {search_prime(n)}')
#     print('OK')
# else:
#     print('Ошибка')