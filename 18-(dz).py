# ЗАДАЧА 18 (семинар 2 - домашнее задание)
# Реализуйте алгоритм перемешивания списка.

import random

def mix_list (list_origin):
    list_mix = list(list_origin)
    size = int(len(list_origin))
    for i in range(size):
        index_rand = random.randint(0, size-1)
        temp = list_mix[i]
        list_mix[i] = list_mix[index_rand]
        list_mix[index_rand] = temp
    return list_mix

list_prime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("исходный список:     ", list_prime)
print("перемешанный список: ", mix_list(list_prime))