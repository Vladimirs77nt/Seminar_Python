# #Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# a = int(input())
# b = int(input())
# if a**2==b or b**2==a:
#   print("yes")
# else:
#   print("no")
#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# a = int(input())
# max = a
# for i in range(5):
#   a = int(input())
#   if a>max:
#     max = a
# print(max)
a = input()
list_num = a.split(",")
print(max(list_num))
