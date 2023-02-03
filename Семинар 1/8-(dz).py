# Задача №8
# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

# Пример:
#  x=34; y=-30  -> 4
#  x=2; y=4     -> 1
#  x=-34; y=-30 -> 3

X = int(input("Введите координату X: "))
Y = int(input("Введите координату Y: "))

if X>0 and Y>0:
    print ("Введены координаты 1-ой четверти")
if X<0 and Y>0:
    print ("Введены координаты 2-ой четверти")
if X<0 and Y<0:
    print ("Введены координаты 3-ей четверти")
if X>0 and Y<0:
    print ("Введены координаты 4-ой четверти")
if X == 0 and Y == 0:
    print ("Введены координаты 0, 0")
elif X == 0:
    print ("Введены координаты точки, находящейся на оси Y")
elif Y == 0:
    print ("Введены координаты точки, находящейся на оси X")