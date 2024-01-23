# Множества или Set

# Множество - структура данных, которая представляет собой неупорядоченную коллекцию уникальных элементов.

# Создание:
a = {1, 2, 3, 4, 5}

# Создание при помощи set():
a = set('Hello')
b = set([1, 2, 3, 4, 5])

# Длина:
a = {4, 5, 6, 2, 1, 3}
print(len(a))

# Объединение (| or union):
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c = a | b # -> c: 1, 2, 3, 4, 5, 6, 7
print(a | b)
print(a.union(b))

# Пересечение (& or intersection):
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c = a & b # -> c: 3, 4, 5
print(a & b)
print(a.intersection(b))

# Задача:
# Пользователь вводит текст
# Программа принимает данный текст и выводит:
# - длину текста
# - количество различных букв в тексте
# - все различные буквы текста

# Решение:
text = input() # считывание текста, вводимого пользователем, и запись его в переменную text
result = set(text) # создание множество на основе введённого текста
print(len(text)) # длина введённого текста
print(len(result)) # длина множества, то есть количество различных букв в тексте
print(*result) # множство, то есть все различные буквы введённого текста

# Задача:
# Пользователь вводит два слова
# Программа выводит общие для этих слов буквы

# Решение:
first, second = set(input()), set(input()) # считываем и сразу создаем множества на основе входных данных
print(first & second) # находим пересечение

# Задача:
# Пользователь вводит два слова
# Программа выводит все буквы, которые используются в этих словах, и их количество

# Решение:
first, second = set(input()), set(input()) # считываем и сразу создаем множества на основе входных данных
result = first | second # находим пересечение
print(result)
print(len(result))