# Alekseeva Elena

# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = int(input("Введите кол-во чисел? "))
d = int(input("Какую цифру посчитать? "))
count = 0   # счётчик
for i in range(1, n + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10

print(f"Было введено {count} цифр {d}")