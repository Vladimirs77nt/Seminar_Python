# 19. Реализуйте алгоритм задания случайных чисел без использования
# встроенного генератора псевдослучайных чисел. n вводит пользователь
# вывести рандомное число в диапазоне от 0 до n

import datetime
def random_int(num):
    rand = datetime.datetime.now().microsecond/10**6
    return int(num*rand)

n = int(input("Введите число n: "))
a = random_int(n)
print(a)