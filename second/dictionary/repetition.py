# ПОВТОРЕНИЕ


# Задача:
# Создайте словарь, в котором будут храниться следующие пары:
# Имя человека в кабинете - его возраст

# Решение:
progers = {
    'Самат': 14,
    'Халид': 12,
    'Азамат': 11,
    'Максим': 12,
    'Искандер': 12,
    'Михаил': 13,
    'Я': 19
}

del progers['Я']
print('Я' in progers)
print(progers)

for proger in progers:
    print(proger, '-', progers[proger])

# Выведите средний возраст всех людей в кабинете
sum = 0
for i in progers:
    sum += progers[i]
print(sum / len(progers))
