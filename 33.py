# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

print()
k = int(input("Задайте натуральную степень k: "))
a = {i: randint(0,100) for i in range(k,0,-1)}  # формирование списка (словаря) коэффициентов многочлена степени k (Random)
a[0] = randint(0,100)                           # свободный член
print("Коэффициенты (по степени): ", a)
polynomial = " = 0"
if a[0] > 0:
    polynomial = str(a[0]) + polynomial
for i in range(1,k+1):
    if a[i]!=0:
        polynomial = str(a[i]) + "*x**" + str(i) + " + " + polynomial
print("Многочлен: ", polynomial)