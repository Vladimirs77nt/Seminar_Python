# ЗАДАЧА 14 (семинар 2 - домашнее задание)
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# ВАРИАНТ РЕШЕНИЯ №3 - работаем сразу с числом FLOAT
# сначала вычисляем число до точки, и число после точки
# потом с помощью функции подсчитываем цифры

# функция 1 - подсчет цифр в целом числе
def sum_digit(num):     
    num = int(num)
    summ_digit = int(0)
    while num>0:
        summ_digit += int(num%10)
        num = num//10
    return summ_digit

# функция 2 - перевод цифр после точки в целое число
def digit_down(number):
    number = float(round(number,10))
    res = int(0)
    sum_null = int(0)
    while sum_null < 10:
        number = round(number * 10, 10)
        a = int (number)
        res = res*10 + a
        number -= a
        sum_null += 1
    return res

# программа
num = float(input("Введите любое вещественное число: "))
num1 = int(num)                         # число до точки
num2 = num - num1                       # число после точки (не обработанное)
num2 = digit_down(num2)                 # число после точки (преобразованное)
summ = sum_digit(num1) + sum_digit(num2)
print("Сумма всех цифр: ", summ)