# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

import math
num = math.pi               # исходное число
print(num)
print("Вычисление числа c заданной точностью d")
d = float(input("введите d: "))
n = 0
while d<1:
    d *= 10
    n+=1
num_d = round(num,n)        # число округленное с заданной точностью
print(num_d)