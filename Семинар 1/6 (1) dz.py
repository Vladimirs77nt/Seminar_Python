# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print("Введите цифру дня недели (1-7): ", end ="")
num = int(input())
if 1<=num<=5:
    print ("-> нет (будни)")
elif 6<=num<=7:
    print ("-> да (выходной)")
else:
    print ("Введены неверные данные")