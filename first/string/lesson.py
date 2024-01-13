# STRING ИЛИ СТРОКОВЫЙ ТИП ДАННЫХ


# Строки - это сложный тип данных, представляющий собой последовательность символов.
# Объявление переменной строкового типа данных
text = 'Hello world!'

# Вывод строки
print(text)
print('Текст')

# Считывание текста, вводимого пользователем
text = input('Введите текст: ')

# Обращение к конкретному элементу строки
# Напомню, что индекс начинается с 0
# Так же можно обращаться к элементам строки через обратные индексы: -3, -5, -1
# строка[индекс]
text[4]
text[-2]

# Длина строки
# len(строка)
len(text)
len('Текст')

# Срез строки
# строка[a:b:c]
# a - индекс, с которого нужно начать, b - индекс, которым нужно закончить, с - шаг
# если не указывать параметр а, он примет дефолтное значение: индекс первого элемента, то есть 0
# если не указывать параметр b, он примет дефолтное значение: индекс последнего элемента, то есть len(text) - 1
# если не указывать параметр с, он примет дефолтное значение: 1, то есть в срез будет включено каждый элемент на заданном промежутке
text[1:5]
text[:3]
text[3:]
text[0:5:2]

# Задача:
# Пользователь вводит слово, а программа должна вывести первую и последнюю букву этого слова.

# Решение:
word = input('Введите слово: ')
print(word[0], word[-1])

# Задача:
# Пользователь вводит слово, а программа должны вывести строку задом наперёд.

# Решение:
text = input('Введите слово: ')
text = text[::-1] # благодаря параметру шаг мы можем перевернуть строку. дада, шаг тоже может быть отрицательным числом.
print(text)