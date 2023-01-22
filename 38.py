# 38) Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100
# Имеется список имен сотрудников из 10 элементов
# Сопоставьте каждому имени сотрудника его id, и выведите получившийся список.
# Выведете имена сотрудников, получившие нечетное id. Решить с помощью zip,filter,lambda

import random
id = [random.randint(1, 100) for i in range(10)]
name = ["Иван", "Дмитрий", "Сергей", "Евгений", "Владимир", "Виктор", "Сергей", "Алексей", "Артем", "Жанн"]
data = list(zip(id, name))
print("Список: ")
print(data)

# 1 вариант - с помощью цикла FOR
print()
print("с помощью ЦИКЛА")
data2 = []
for i in data:
    if i[0]%2: data2.append(i)
print (data2)

# 2 вариант - с помощью Filter/Lambda
print()
print("с помощью FILTER")
data2 = list(filter(lambda x: x[0]%2==1, data))
print (data2)