# Задача:
    # Напишим программу, которая запросит фамилию, имя и возраст,
    # а затем выведет соответствующее сообщение:
    # Здравствуйте, {фамилия}{имя}!
    # Вам {возраст} лет.

# Решение:
name = input()
surname = input()
age = int(input())
print('Здравствуйте,', surname, name + '!')
print('Вам', age, 'лет.')

# Задача:
    # Запросите у пользователя возраст, а затем напечайте:
    # Вам до 100 лет ещё {посчитать} лет.

# Решение:
age = int(input())
print('Вам до 100 лет ещё', 100 - age, 'лет.')

# Задача:
    # Напишите программу, в которой пользователь вводит свой год рождения и текущий год.
    # Программа вычисляет возраст пользователя и выводит соответствующее сообщение.

    # Ввод:
    # 2000
    # 2022

    # Ответ:
    # Ваш возраст: 22 года

# Решение:
year_of_birth = int(input())
current_year = int(input())
print('Ваш возраст:', current_year - year_of_birth)

# Задача:
    # Напишите программу, в которой пользователь вводит количество денег в какой-то валюте
    # и курс этой валюты в рублях.
    # A в ответ получает сообщение сколько это в рублях.

    # Ввод:
    # 2
    # 60

    # Ответ:
    # У вас 120 рублей.

# Решение:
money = int(input())
currency = float(input())
print('У вас', money * currency, 'рублей.')
