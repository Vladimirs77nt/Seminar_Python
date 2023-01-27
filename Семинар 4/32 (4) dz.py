# Задача 32. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
b = randint(5,12)    # длина списка Random (от 5 до 12)
num = [randint(0,10) for i in range(b)]
print("исходная последовательность чисел: ", num)
num_nodouble = []
for i in num:
    if num.count(i) == 1:
        num_nodouble.append(i)
print(num_nodouble)