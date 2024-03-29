# МЕТОДЫ СТРОК
text = 'какие-то слова и ещё раз какие-то слова'


# Методы index() и rindex()
# находит индекс первого и последнего вхождения текста, передаваемого в эти методы
# если передаваемого текста нет в строке, то результатом метода будет ошибка: не удалось найти подстроку
print(text.index('-то')) # 5
print(text.rindex('-то')) # 30
# print(text.index('два')) # ошибка: substring not found

# Методы find() и rfind()
# находит индекс первого и последнего вхождения текста, передаваемого в эти методы
# если передаваемого текста нет в строке, то результатом метода будет -1
print(text.find('слова')) # 9
print(text.rfind('слова')) # 34
print(text.find('  ')) # -1

# Методы upper() и isupper()
# первое - переводит все буквы строки в верхний регистр,
# второе - проверяет находятся ли все буквы в верхнем регистре и возвращает True или False
print(text.upper()) # КАКИЕ-ТО СЛОВА И ЕЩЁ РАЗ КАКИЕ-ТО СЛОВА
print(text.isupper()) # False
text = text.upper() # перевели все буквы в верхний регистр и сохранили изменения путём перезаписи переменной
print(text.isupper()) # True

# Метод lower() и islower()
# первое - переводит все буквы строки в нижний регистр
# второе - проверяет находятся ли все буквы в нижнем регистре и возвращает True или False
print(text.lower()) # какие-то слова и ёще раз какие-то слова
print(text.islower()) # False
text = text.lower() # перевели все буквы в нижний регистр и сохранили изменения путём перезаписи переменной
print(text.islower()) # True

# Метод title() istitle()
# первое - переводит все первые буквы каждого слова в строке в верхний регистр
# второе - проверяет находятся ли все первые буквы каждого слова строки в верхнем регистре и возвращает True или False
print(text.title()) # Какие-то Слова И Ещё Раз Какие-то Слова
print(text.istitle()) # False
text = text.title() # перевели первые буквы каждого слова строки в верхний регистр и записали изменения в переменную
print(text.istitle()) # True

# А теперь объясню зачем нам нужно сохранять изменения в переменной
# Дело в том, что результатом выполнения этих методов не являются изменения самой строки, результатом является изменная копия данной строки.
# Поэтому при выводе строки с использованием метода, выводится измененная строка, то есть измененная копия исходной строки
# А при выполнении такой строки: text.lower(), не происходит ничего, так как мы ничего не делаем с изменённой копией исходной строки

# Задача:
# Напишите программу, в которой пользователь вводит “Меня зовут Иван Иванович, мой адрес Город набережные Челны, год рождения рождения 2000”,
# а программа выводит сообщение об индексе первого вхождения подстроки “зовут”, “адрес”, “год”.

# Решение:
text = 'Меня зовут Иван Иванович, мой адрес Город набережные Челны, год рождения рождения 2000'
print(text.find('зовут'))
print(text.find('адрес'))
print(text.find('год'))

# Задача:
# Напишите программу, в которой пользователь вводит текст “Кто не работает, тот не ест”,
# а программа переводит этот текст в нижний регистр и в верхний регистр.

# Решение:
text = 'Кто не работает, тот не ест'
print(text.lower())
print(text.upper())
