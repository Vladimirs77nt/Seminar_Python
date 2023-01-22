# ЗАДАЧА 14 (семинар 2 - домашнее задание)
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# ВАРИАНТ РЕШЕНИЯ №2 - замудренный: метод split + функция для подсчета цифр в целом числе

def sum_digit(num):
    num = int(num)
    summ_digit = int(0)
    while num>0:
        summ_digit += int(num%10)
        num = num//10
    return summ_digit

num = input("Введите любое вещественное число: ")
num = num.split(".")
len = int(len(num))
summ = int(0)
for i in range(len):
    num[i] = int(num[i])
    summ += sum_digit(num[i])
print("Сумма всех цифр: ", summ)