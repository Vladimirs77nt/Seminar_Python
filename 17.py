# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input("Введите целое число N больше 0: "))
list = list(range(-N, N+1))                         # создаем список [-N, N]
print(list)                                         
f = open('text.txt','r')                            # читаем файл с индексами
list_index = f.readlines()
f.close()
list_index = [i.rstrip() for i in list_index]       # удаляем знаки новой строки
list_index = [int(i) for i in list_index]           # преобразуем строку в числа
print("индексы: ", list_index)
list2 = [list[i] for i in list_index]               # создаем новый список с нужными элементами
print("элементы по индексам: ", list2)
result = int(1)
for i in list2:                                     # по циклу перемножаем элементы
    result *= i
print("Произведение элементов: ", result)