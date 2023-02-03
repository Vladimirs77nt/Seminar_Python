# Задача №14 (решение от Артура)
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n = input()
# summ = 0
# for i in n:
#     if i.isdigit():
#         summ+=int(i)
# print(summ)

n = float(input())
len_num = len(str(n))-1
summ=0
while n!=int(n):
    n= round(n*10,len_num)
    print(n)
while n>0:
    summ+=n%10
    n = n//10
print(summ)