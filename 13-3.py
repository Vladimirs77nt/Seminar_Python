# 13. (вариант 3) Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Пример:
# Строка - "dabccabccabcc"
# Подстрока - "ab"
# Количество вхождений - 3

# решение от Артема (одно из)
a = input("Введите строку: ")
b = input("введите текст для поиска: ")
count = 0
dif_len = int(len(a)-len(b))
len = int(len(b))

for i in range(dif_len+1):
    if a[i:i+len] == b:
        count += 1
print("Кол-во вхождений: ", count)