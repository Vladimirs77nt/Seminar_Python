# 13. (вариант 2) Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Пример:
# Строка - "dabccabccabcc"
# Подстрока - "ab"
# Количество вхождений - 3

#- интересное решение 13 задачи

my_string = input('Введите строку: ')
b = input('Введите подстроку: ')
start = -1
count = 0
while True:
    start = my_string.find(b, start+1)
    if start == -1:
        break
    count += 1
print("Количество вхождений символа в строку: ", count)