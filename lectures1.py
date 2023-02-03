# Переменные. Типы данных справедливы
# int, float, boolean, str
# list и др.
# Python – язык с динамической типизацией
# value = 2809
# name = 'Sergey'

# Ввод и вывод данных. Преобразование типов

# print('Введите а');
# a = input()
# print('Введите b');
# b = input()
# print(a, b)
# print('{} -- {}'.fotmat(a, b))

# print('Введите а');
# a = input() # 10
# print('Введите b');
# b = input() # 20
# c = a + b
# print(a, ' + ', b, ' = ', c)

# print('Введите а');
# a = int(input())
# print('Введите b');
# b = int(input())
# c = a + b
# print(a, ' + ', b, ' = ', c)
# print('{} + {} = {}'.format(a, b, c))

# print('Введите а');
# a = float(input())
# print('Введите b');
# b = float(input())
# c = a + b
# print(a, ' + ', b, ' = ', c)

# a = int(input('Введите а: ')) # 11
# b = int(input('Введите b: ')) # 22
# c = a + b
# print('{} + {} = {}'.format(a, b, c)) # 11 + 22 = 33

# a = int(input('Введите \nа: '))
# b = int(input('Введите \nb: '))
# c = a + b
# print('{} + {} = {}'.format(a, b, c))

# Арифметические операции

# exp1 = 2**3 - 10 % 5 + 2*3
# exp2 = 2**3 - 10 / 5 + 2*3
# print(exp1)  # 14.0 или 14
# print(exp2)  # 12.0 или 12

# exp1 = 2**3 - 10 % 5 + 2*3
# exp2 = (2**3) - (10 / 5) + (2*3)
# print(exp1)  # 14.0 или 14
# print(exp2)  # 12.0 или 12

# Сокращённые операции и операции присваивания

# iter = 2
# iter += 3    # iter = iter + 3
# iter -= 4    # iter = iter - 4
# iter *= 5    # iter = iter * 5
# iter /= 5    # iter = iter / 5
# iter //= 5   # iter = iter // 5   - целочисленное деление
# iter %= 5    # iter = iter % 5    - остаток от деления
# iter **= 5   # iter = iter ** 5   - возведение в степень

# a, b, c = 1, 2, 3
# # a: 1 b: 2 c: 3
# print('a: {} b: {} c: {}'.format(a, b, c))
 
# +92./range(*(1,5,2))  - округление

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# Управляющие конструкции: if, if-else

# if condition:
#     # operator 1
#     # operator 2
#     # ...
#     # operator n
# else:
#     # operator n + 1
#     # operator n + 2
#     # ...
#     # operator n + m

# username = input('Введите имя: ')
# if(username == 'Маша'):
#     print('Ура, это же МАША!');
# else:
#     print('Привет, ', username);

# if condition1:
#     # operator
# elif condition2:
#     # operator
# elif condition3:
#     # operator
# else:
#     # operator 

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# Управляющие конструкции: while

# while condition:
#     # operator 1
#     # operator 2
#     # . . .
#     # operator n

# original = 35782
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print (original)
# else:
#     print("Пожалуй")
#     print("хватит )")
# print (inverted)

# Управляющие конструкции: for
# for i in enumeration:
#     # operator 1
#     # operator 2
#     # . . .
#     # operator n

# for i in 1, -2, 3, 14, 5:
#     print (i)
# # 1
# # -2
# # 3
# # 14
# # 5

# Управляющие конструкции: for
# Знакомьтесь – range
# r = range(5)           # range(0, 5)
# r = range(2, 5)        # range(2, 5)
# r = range(-5, 0)       # range(-5, 0)
# r = range(1, 10, 2)    # range(1, 10, 2)
# r = range(100, 0, -20) # range(100, 0, -20)

# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#     print(i)
# # 100 80  60 40 20
# for i in range(5):
#     print(i)
# # 0 1 2 3 4

# Вложенные циклы
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'съешь ещё этих мягких французских булок'
# print(len(text))       # 39     - длина строки
# print('ещё' in text)   # True   - встрачется ли с тексте
# print(text.isdigit())  # False  - текст - это цифры?
# print(text.islower())  # True   - текст - в нижнем регистре?
# print(text.replace('ещё','ЕЩЁ'))  # - замена в тексте
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])   # c    - вывесим нулевой символ
# print(text[1])   # ъ    - вывести первый символ (отсчет идет с нуля!)
# print(text[len(text)-1])  # к   - длина текста - 1
# print(text[-5])  # б            - пятый с конца
# print(text[:])   # print(text)  вывести весь текст
# print(text[:2])  # съ     - вывести с 0 до 1 (2-1)
# print(text[len(text)-2:])  # ок - вывести последние два
# print(text[2:9])  # ешь ещё     - вывести со 2 до 8 (9-1)
# print(text[6:-18])  # ещё этих мягких   - вывести с 6 до 18* (*с конца)
# print(text[0:len(text):6])  # сеикакл   - вывести с с шагом 6
# print(text[::6])  # сеикакл             - вывести с с шагом 6
# text = text[2:9] + text[-5] + text[:2] # ... - соединение символов
# print(text)

# Список – пронумерованная, изменяемая коллекция объектов произвольных типов 
# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)    # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)   # red green blue
# for e in colors:
#     print(e*2)   # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red')    # найти и удалить ПЕРВЫЙ элемент со значением "red"
# del colors[0]           # удалить элемент с индексом 0

# colors = ['red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green', 'blue']
# print (colors)
# colors.remove('red') 
# print (colors)
# colors.remove('red') 
# print (colors)
# colors.remove('red') 
# print (colors)

# Функции. Это фрагмент программы, используемый многократно

# def function_name(x):
# # body line 1
# # . . .
# # body line n
#     # optional return  

# Функции
# def f(x):
#     return x**2

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# print(f(1))         # Целое
# print(f(2.3))       # 23
# print(f(28))        # None
# print(type(f(1)))   # str
# print(type(f(2.3))) # int
# print(type(f(28)))  # NoneType