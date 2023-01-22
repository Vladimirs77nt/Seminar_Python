# Задача 39 (2). Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно,
# необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, каждый
# из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, на которую мы хотим
# поставить крестик или нолик, и проверку на победу (стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

def print_3x3 (x):
    print ("|-----------|")
    for i in range(3):
        s = "|"
        for j in range(3):
            if x[i*3+j] == -1:
                s+="   |"
            elif x[i*3+j] == 1:
                s+=" X |"
            else:
                s+=" 0 |"
        print (s)
        print ("|-----------|")

def proverka (x):
    if (x[0] == x[1] == x [2]) and x[0]>=0: return True
    if (x[3] == x[4] == x [5]) and x[3]>=0: return True
    if (x[6] == x[7] == x [8]) and x[6]>=0: return True
    if (x[0] == x[3] == x [6]) and x[0]>=0: return True
    if (x[1] == x[4] == x [7]) and x[1]>=0: return True
    if (x[2] == x[5] == x [8]) and x[2]>=0: return True
    if (x[0] == x[4] == x [8]) and x[0]>=0: return True
    if (x[2] == x[4] == x [6]) and x[2]>=0: return True
    return False

import random
pole = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
conf_igrok = [0 ,0]
igrok = random.randint(1,2)
print ("Первым играет игрок №", igrok, ", (играет крестиками)")
znak = 1
conf_igrok [igrok-1] = 1  # 0 - играет ноликами, 1 - играет крестиками
count = 0
print_3x3 (pole)

while True:
    if znak == 1: znak_str = "крестик"
    else: znak_str = "нолик"
    while True:
        print("Игрок", igrok, " - на какую клетку поставишь", znak_str, "? укажи ряд и столбец):")
        n1 = int(input())
        n2 = int(input())
        if n1>0 and n1<4 and n2>0 and n2<4:
            if pole[(n1-1)*3+(n2-1)] >= 0:
                print ("Эта клетка уже заполнена, укажи другую клетку!!!")
                print ()
            else: break
        else: print("- неверно указан ряд или столбец!")
    pole[(n1-1)*3+(n2-1)] = znak
    print_3x3 (pole)
    print()
    if proverka (pole):
        print ("Победа!!! Победил игрок №", igrok)
        print()
        break
    count += 1
    if count > 8:
        print ("Все клетки заполнены, игра завершена. НИЧЬЯ")
        print ()
        break
    if igrok == 2: igrok = 1
    else: igrok = 2
    if znak == 1: znak = 0
    else: znak = 1