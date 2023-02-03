# 35) Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda.
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]

# # А) МОЕ РЕШЕНИЕ
# a = [1, 2, 3, 5, 7, 8, 9, 10]
# print(type(a), a)
# b = [1, 2, 4, 8, 9]
# print(type(b), b)

# c = []
# for i in a:
#     c = c + list(filter(lambda j: j==i, b))
#     # c = c + (list(lambda b[j]: b[j]==i for j in range(len(b))))
# print ("Пересечение:", type(c), c)

# # Б) РЕШЕНИЕ ОТ АРТУРА
a = [1, 2, 3, 5, 7, 8, 9, 10]
b = [1, 2, 4, 8, 9]
c = list(filter(lambda j: j in a, b))
print (c)