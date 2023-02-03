# Задача №45.
# Найти сумму чисел списка стоящих на нечетной позиции

# ** Ранее это была задача № 22 к семинару №3


a = [1, 21, 33, 45, 5, 6, 7, 8, 9, -10]
print (a)
print ()

# РЕШЕНИЕ ВАРИАНТ 1
print("ВАРИАНТ 1 - из семинара 3 (задача 22) - с циклом")
summ1 = 0
for indx, value in enumerate(a):
    if indx%2 == 1: summ1 += value
print ("сумма =", summ1)
print()

# РЕШЕНИЕ ВАРИАНТ 2 - с помощью sum, filter, lambda, enumerate
print("ВАРИАНТ 2 - с помощью sum, filter, lambda, enumerate")
summ2 = sum(list(i[1] for i in (filter((lambda x: x[0]%2 == 1), enumerate(a)))))
print ("сумма =", summ2)
print()