# ЗАДАЧА 26 (семинар 3 - домашнее задание)
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]

num = int(input("Введите целое число: "))
if num<0: num = -num
fibonacci = [0]
if num > 0:
        fibonacci = [1, 0, 1]
fib1, fib2 = 0, 1
n = -1
for i in range(num-1):
    fib1, fib2 = fib2, fib1 + fib2
    fibonacci.append(fib2)
    fibonacci.insert(0,fib2*n)
    n = -n
print(fibonacci)