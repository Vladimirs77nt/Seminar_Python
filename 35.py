<<<<<<< HEAD
# Задача 35. Даны два файла, в каждом из которых находится запись
# многочлена. Задача - сформировать файл, содержащий сумму многочленов.
=======
# Задача 35. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
>>>>>>> 151a82f8e2c6d95205fd1fb1b192e6e45e9f6981

from random import randint

# функция создания файла с рандомными многочленами (от 3 до 6 степени)
def create_file_polynom(name):
    polynomial = polynom_random_create(randint(3, 6))
    f = open(name, 'w')
    f.write(polynomial)
    f.close()
    return polynomial

# функция чтения файла с многочленами
def read_file_polynom(name):
    f = open(name,'r')
    polynomial_text = str(f.readlines())
    polynomial_text = polynomial_text[2:-2]
    f.close()
    return polynomial_text

# функция рандомного создания многочлена k-степени
def polynom_random_create(k):
    a = [randint(0,100) for i in range(k)]
    n = randint(0,100)
    polynomial = " = 0"
    if n > 0: polynomial = str(n) + polynomial
    for i in range(len(a)):
        if a[i]!=0:
            polynomial = str(a[i]) + "*x**" + str(i+1) + " + " + polynomial
    return polynomial

# функция формирования списка коэффициентов многочлена из строковой переменной
def polynom_index_text(polynomial):
    a = ""
    for i in polynomial:
        if i == "=":
            break
        elif i != " " and i != "]" and i != "[" and i != "'":
            a = a + i
    a = a.split("+")
    a_index = {}                        # пустой список (словарь) для записи коэффициентов
    for i in range(len(a)):
        s = a[i]
        b = s.find("**")
        if b>0:
            index = int(s[:b-2])        # коэффициент многочлена
            digree = int(s[b+2:])       # степень многочлена
            a_index[digree] = index
        else:
            index = int(s)
            a_index[0] = index     # запись свободного члена
    return a_index

# функция создания многочлена k-степени с заданными коэффициентами
def polynom_create(index):
    polynomial = " = 0"
    if index[0] > 0:
        polynomial = str(index[0]) + polynomial
    index = dict(sorted(index.items()))
    for k, v in index.items():
        if v!=0 and k!=0:
            polynomial = str(v) + "*x**" + str(k) + " + " + polynomial
    return polynomial

# функция складывания коэффициентов двух словарей
def polynom_summ(a,b):
    c = a.copy()
    for k, v in b.items():
        c[k] = c.get(k, 0) + v
    # sorted(c.items())             # сортировка ключей
    c = dict(sorted(c.items(), reverse=True))
    return c

# ОСНОВНАЯ ЧАСТЬ ПРОГРАММЫ

<<<<<<< HEAD
# 1. создаем два новых файла со рандомными многочленами - рабочие файлы: "text_1.txt" и "text_2.txt"
# т.к. файлы уже есть - закомментировал... // но можно проверить как работает
# print()
# print("Запись файлов...")
=======
# 1. создаем два новых файла со рандомными многочленами
#  - рабочие файлы: "text_1.txt" и "text_2.txt"
# т.к. файлы уже есть - я закомментировал этот блок... но можно проверить как работает
# print()
# print("Создание многочленов и запись файлов...")
>>>>>>> 151a82f8e2c6d95205fd1fb1b192e6e45e9f6981
# polynomial_1 = create_file_polynom('text_1.txt')
# polynomial_2 = create_file_polynom('text_2.txt')

# 2. читаем два файла с готовыми многочленами - рабочие файлы: "text_1.txt" и "text_2.txt"
print()
print("Чтение файлов...")
polynomial_text_1 = read_file_polynom('text_1.txt')
print("Первый многочлен: ", polynomial_text_1)
polynomial_text_2 = read_file_polynom('text_2.txt')
print("Второй многочлен: ", polynomial_text_2)

# 3. формируем 2 таблицы (словари) коэффициентов прочитанных многочленов
print()
print("Определяем коэффициенты по степеням...")
index_1 = polynom_index_text(polynomial_text_1)
print("Коэффициенты 1-го многочлена: ", index_1)
index_2 = polynom_index_text(polynomial_text_2)
print("Коэффициенты 2-го многочлена: ", index_2)

# 4. суммируем 2 таблицы (словари) коэффициентов прочитанных многочленов
print()
print("Суммируем коэффициенты по степеням...")
summ = polynom_summ (index_1, index_2)     # сумма коэффициенто
print ("-> Сумма коэфиициентов: ", summ)

# 5. создаем суммирующий многочлен
print()
print("Итак, результат...")
polynomial_text = polynom_create (summ)
<<<<<<< HEAD
print("Сумма многочленов: ", polynomial_text)
=======
print("Сумма многочленов: ", polynomial_text)

# 6. создаем файл "text_.txt" с суммирующим многочленом
f = open("text_3.txt", 'w')
f.write(polynomial_text)
f.close()
>>>>>>> 151a82f8e2c6d95205fd1fb1b192e6e45e9f6981
