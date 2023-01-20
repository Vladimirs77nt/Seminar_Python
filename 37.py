# 37) Имеется упорядоченный список:
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Перебрать все элементы этого списка с помощью функций enumerate
# и элементы стоящие на главной диагонали (имеющие равные индексы), превратить в нули.

# # А) ВАРИАНТ 1
# array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(array)
# for indx, val in enumerate(array):
#     val[indx] = 0
# print(array)

# Б) ВАРИАНТ 2
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(array)
for indx, val in enumerate(array):
    val[indx] = 0
print(array)
