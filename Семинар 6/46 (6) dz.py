# Задача №46.
# Найти произведение пар чисел списка (парой считаем первый и последний, второй предпоследний и тд)

# ** Ранее это была задача № 23 к семинару №3

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

a = [3, 1, 5, 9, 5, 1, 4, 5]
print(a)
print ()

# РЕШЕНИЕ ВАРИАНТ 1
print("ВАРИАНТ 1 - из семинара 3 (задача 23) - с циклом")
c = []
l = int(len(a))
for i in range(int(l/2 + 0.5)):
    b = a[i] * a[l-i-1]
    c.append(b)
print(c)
print()

# РЕШЕНИЕ ВАРИАНТ 2 - с помощью LIST COMPREHENSION
print("ВАРИАНТ 2 -  - с помощью LIST COMPREHENSION")
c = list(a[i]*a[len(a)-i-1] for i in range(int((len(a)+1)/2)))
print(c)
print()