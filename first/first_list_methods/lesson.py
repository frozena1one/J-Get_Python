# МЕТОДЫ СПИСКОВ. ПЕРВЫЙ УРОК


nums = [100, 1056, 54, 10, 1, 981, 613, 490, 999, 777]
# Наибольшее значение:
print(max(nums)) # 1056

# Наименьшее значение:
print(min(nums)) # 1

# Сумма элементов списка:
print(sum(nums)) # 5081

# Переворот списка
print(reversed(nums)) # <list_reverseiterator object at 0x7f266d7c7910>
print(list(reversed(nums))) # [777, 999, 490, 613, 981, 1, 10, 54, 1056, 100]

# Пояснение
# При использовании метода reversed() результат его работы необходимо обернуть в список, так как иначе мы получим лишь экземляр класса.
# Экземпляр класса понятие из ООП, которые мы будем изучать позже.
# Так что пока просто запомните, что там где reversed(), там и list().

# Cортировка списка:
print(sorted(nums)) # сортировка по возрастанию
print(sorted(nums, reverse=True)) # сортировка по убыванию

# Задача:
# Пользователь вводит список имён. Программа должна перевернуть этот список.

# Решение:
names = list(map(str, input().split())) # эта конструкция считывает данные и записывает в список. просто запомните её.
print(list(reversed(names)))

# Задача:
# Пользователь вводит список чисел.
# Программа должна напечатать наименьшее и наибольшее значения, сумму всех элементов и отсортированный по убыванию список.

# Решение:
nums = list(map(int, input().split()))
print(min(nums))
print(max(nums))
print(sum(nums))
print(sorted(nums, reverse=True))
