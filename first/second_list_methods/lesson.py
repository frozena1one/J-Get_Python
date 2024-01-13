# МЕТОДЫ СПИСКОВ. ВТОРОЙ УРОК


# join()
vowels = ["a", "e", "i", "o", "u"]
vowels_str = ",".join(vowels) # 'a,e,i,o,u'
print("Строка гласных:", vowels_str)

# list()
l = list('Строка')
print(l) # ['С', 'т', 'р', 'о', 'к', 'а']

# append()
l = list('Строка')
l.append("A") # 'СтрокаА'
print(l)

# extend()
l = list("Строка")
v = list("Арбуз")
l.extend(v) # ['С', 'т', 'р', 'о', 'к', 'а', 'А', 'р', 'б', 'у', 'з']
print(l)

# insert()
l = list("Строка")
l.insert(4, "ч") #  ['С', 'т', 'р', 'о', 'ч', 'к', 'а']
print(l)

# pop()
l = list("Строчка")
l.pop(4) # ['С', 'т', 'р', 'о', 'к', 'а']
print(l)

# count()
l = list("албания")
print(l.count("а")) # 2

# Задача:
# Дана строка “Слушать”.
# Напишите программу, которая преобразует строку в список, добавляет в конец списка букву “ся”,
# а затем преобразует это в обратно в строку.

# Решение:
string = 'Слушать'
list_letters = list(string)
list_letters.extend(['с', 'я'])
string = ''.join(list_letters)
print(string)

# Задача:
# Дана строка “Вход”.
# Напишите программу, которая преобразует строку в список, и делает из слова “вход”, слово “выход”,
# а затем выводит список как строку,  в которой буквы разделены пробелами.

# Решение:
string = 'Вход'
list_letters = list(string)
list_letters.insert(1, 'ы')
string = ''.join(list_letters)
print(string)
