# 2. Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

num = float(input("Введите дробное число: "))
num1 = num*100//10
num2 = (num*10//10)*10
if (num - round (num,0)) != 0:
    print (int(num1-num2))
else:
    print ("Нет")