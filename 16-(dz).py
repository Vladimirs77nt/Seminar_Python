# ЗАДАЧА 16 (семинар 2 - домашнее задание)
# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 4: {1: 2, 2: 2.25, 3: 2,37 4: 2,44}

num = int(input("Введите целое число больше 0: "))
list = {}
summ = 0
for n in range(1,num+1):
    x = round((1+1/n) ** n,2)
    list[n] = x
    summ += x
print(list)
print("Сумма: ", summ)