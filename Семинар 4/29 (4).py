# 29. Задайте два числа. Напишите программу, которая найдёт
# НОК (наименьшее общее кратное) этих двух чисел.

print("Введите два целых числа")
a = int(input("введите 1-ое число: "))
b = int(input("введите 2-ое число: "))

for i in range(max(a,b),a*b+1,max(a,b)):
    if i % a == 0 and i % b == 0:
        print("НОК = ", i)
        break