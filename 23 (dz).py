# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_num = [2, 3, 4, 5, 6]
print(list_num)
list_res = []
len = int(len(list_num))
for i in range(int(len/2 + 0.5)):
    a = list_num[i] * list_num[len-i-1]
    list_res.append(a)
print(list_res)