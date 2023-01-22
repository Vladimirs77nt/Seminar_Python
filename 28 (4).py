# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

import math

print("Решение квадратного уравнения Ax² + Bx + C = 0")
a = int(input())
b = int(input())
c = int(input())

d = b**2 - 4*a*c
if a!=0:
    if d>0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        print(x1,x2)
    elif d == 0:
        x = -b / (2 * a)
        print(x)
    else:
        print("net korney")
else:
    x = -c/b
print(x)