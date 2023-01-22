# 39 (1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока
# против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет.
# Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил.

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 

# В качестве дополнительного усложнения можно:
#  a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)
#  b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет
#     необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту)

import random
conf = 221
igrok = random.randint(1,2)
print ("Первым играет игрок №", igrok)
conf_igrok = [0 ,0]

while True:
    print ("На столе лежит", conf, "конфет(а)")
    while True:
        print("Игрок", igrok, " - сколько возьмешь конфет? (от 0 до 28): ")
        n = int(input())
        if n>0 and n<29: break
        print("- неверно указано кол-во конфет!")
    if (conf-n) <= 0:
        print("Победа!")
        print("Победил игрок №", igrok)
        break
    conf_igrok [igrok-1] += n
    conf -= n
    if igrok == 2: igrok = 1
    else: igrok = 2