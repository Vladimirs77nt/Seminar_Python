# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.


# Модуль сжатия:
print ("Модуль сжатия")
data = "AAAAAAFDDCCCCCCCAEEEEEEEEE"
print ("Входные данные:", data)
size = len(data)
data_rle = ""
index = 0
while index<size:
    val = data[index]
    count = 1
    while (index+count)<size and (data[index+count] == val):
        count += 1
    data_rle += str(count) + val
    index += count
print ("Выходные данные (сжатие):", data_rle)
print ("")


# Модуль восстановления:
print ("Модуль восстановления")
data_rle = "6A1F2D7C1A9E"
print ("Входные данные (сжатие):", data_rle)
size = len(data_rle)
data = ""
index = 0
while index<size:
    count = int(data_rle[index])
    val = data_rle[index+1]
    data += val*count
    index += 2
print ("Входные данные:", data)
print ("")