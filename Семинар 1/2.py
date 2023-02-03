# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

num1 = int(input ("введите первое число: "))
num2 = int(input ("введите второе число: "))
num3 = int(input ("введите третье число: "))
num4 = int(input ("введите четвертое число: "))
num5 = int(input ("введите пятое число: "))

num_max = num1
if num2 > num_max:
    num_max = num2
if num3 > num_max:
    num_max = num3
if num4 > num_max:
    num_max = num4
if num5 > num_max:
    num_max = num5
print("Максимальное число: ", num_max)