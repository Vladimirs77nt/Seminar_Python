# ЗАДАЧА 15 (семинар 2 - домашнее задание)
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input("Введите целое число больше 0: "))
list = []
factorial = 1
for i in range(1, num+1):
    factorial *= i
    list.append(factorial)
print(list)