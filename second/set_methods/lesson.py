# Методы множества


# Множество - структура данных, которая представляет собой неупорядоченную коллекцию уникальных элементов.


# МЕТОДЫ:

# .add()
# добавление нового элемента во множество:
months = set(["Jan", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])

months.add("Feb")
print(months)


# .remove() и .discard()
# удаление элемента из множества
# разница в этих методах в том, что метод .remove() вызовет ошибку, если элемент, передаваемый в метод,
# не был найден во множестве, а метод .discrard() не будет вызывать ошибку
num_set = {1, 2, 3, 4, 5, 6}
num_set.discard(3)
print(num_set)


# .union() или |
# на самом деле, этот метод может объединять любое количество множеств
x = {1, 2, 3}
y = {4, 5, 6}
z = {7, 8, 9}

output = x.union(y, z)
output = x | y | z

print(output)


# in
# можно проверить элемент на наличие во множестве
months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])

print("May" in months)



# Задача:
# Создайте множество состоящее из Имен ребят, находящихся в этой комнате.
# Напишите команду, которая добавила бы в множество Азат абыя.
# Напишите команду, которая выводит количество людей в множестве.

# Решение:
names = {'Bob', 'Alex', 'Mike', 'John', 'Conor'}
names.add('Азат абый') # добавили Азат абыя во множество
print(names)
print(len(names))


# Задача:
# Дополните программу так, напишите команду, которая удалит из множества Азат абыя.
# Убедитесь, что в множестве Азат абыя нет с помощью метода in.

# Решение:
names = {'Азат абый', 'Alex', 'Bob', 'Mike', 'John', 'Conor'}
names.discard('Азат абый')
print('Азат абый' in names)


# Задача:
# Напишите программу, которая запрашивает пользователя ввести имя прибывшего,
# а программа вносит это имя в множество.
# Дополните программу так, чтобы вносить имя можно было постоянно.

# Решение:
names = {'Азат абый', 'Alex', 'Bob', 'Mike', 'John', 'Conor'}
while True: # вечный цикл
    name = input()
    names.add(name)
    print(names)
    if len(names) > 10:
        break

# Задача:
# Создайте еще одно множество, состоящее из имен ваших друзей
# Напишите программу, которая бы могла дополнить существующее множество множеством ваших друзей.

# Решение:
first = {'Bulat', 'Halid', 'Kamil'}
second = {'Arslan', 'Iskander', 'Misha', 'Maskim'}
result = first.union(second)
print(result)