# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input("Задайте натуральную степень k: "))
a = [randint(0,100) for i in range(k)]  # формирование списка коэффициентов многочлена степени k (Random)
print("коэффициенты: ", a)
n = randint(0,100)  # свободный член
polynomial = " = 0"
if n > 0: polynomial = str(n) + polynomial
for i in range(len(a)):
    if a[i]!=0:
        if i == 0:
            polynomial = str(a[i]) + "*x" + " + " + polynomial
        else:
            polynomial = str(a[i]) + "*x^" + str(i+1) + " + " + polynomial
print(polynomial)