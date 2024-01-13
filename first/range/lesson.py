# RANGE


# Простыми словами, range() позволяет генерировать ряд чисел в рамках заданного диапазона.

# Синтаксис цикла for c использованием range() c 1 аргументом
for i in range(3): # [0, 1, 2]
    print(i)

# Синтаксис цикла for c использованием range() c 2 аргументами
for i in range(5, 11): # [5, 6, 7, 8, 9, 10]
    print(i)

# Синтаксис цикла for c использованием range() c 3 аргументами
for i in range(1, 11, 3): # [1, 4, 7, 10]
    print(i)

# Задача:
# Напишите программу, которая выводит все делящиеся на 3, 6, 12 числа, начиная от 1 заканчивая 100.
# Немного теории: если приглядеться, то можно заметить, что все числа, которые делятся делятся и на 3, и на 6, и на 12,
# будет теми же что и числа, которые делятся на 12.

# Решение:
for i in range(1, 101):
    if i % 12 == 0: # проверяем делится ли число на 12 нацело
        print(i)

# Но можно решить эту задачу и без использования условного оператора, ведь мы в range() начать с первого числа, которое делится на 12,
# то есть начать с 12, закончить 101 и установить шаг 12.
# То есть range(12, 101, 12)
for i in range(12, 101, 12):
    print(i)

# Задача:
# Напишите программу, которая 25 раз выводит сообщение “python”, причем идет нумерация этих чисел начиная 1, заканчивая 25.

# Решение:
for i in range(1, 26):
    print(i, 'python')