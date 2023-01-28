import config
import data_processing as dtp
import controller
import statistics

def print_student(data): # входная переменная data_student
    print()
    print("Список студентов")
    print("-"*43)
    print("|ID студента|     Имя      |   Фамилия    |")
    print("-"*43)
    for i in data: print("|{0:^11}|{1:^14}|{2:^14}|".format(i[0], i[1], i[2]))
    print("-"*43)
    print()

def print_lesson(): # список учебных предметов в школе
    print()
    print("Список учебных предметов в школе:")
    for indx, item in enumerate(config.lesson_list):
        print((indx+1), item)
    print()

# ПЕЧАТЬ ЖУРНАЛА ОЦЕНОК ДЛЯ КОНКРЕТНОГО УЧЕНИКА
def print_diary(id_student): # входная переменная ID студента
    dsd = dtp.student_diary(id_student)
    index = dtp.index_ID
    if index < 0: return
    data = dtp.data_student[index]
    name = data[1]
    fam = data[2]
    if dsd == []:
        print("У студента", name, fam, "оценок нет")
        return
    print()
    print("Дневник студента:", name, fam)
    print("-"*34)
    print("| предмет урока      | оценки")
    print("-"*34)
    for i in dsd: print("|{0:^20}|{1}".format(config.lesson_list[i[1]], i[2:]))
    print("-"*34)

# 2) Вывод средней оценки ученика по одному предмету
def print_average(id_student, lesson):
    dsd = dtp.student_diary(id_student) # загружаем журнал оценок для студента
    index = dtp.index_ID
    if index < 0: return
    data = dtp.data_student[index]
    name = data[1]
    fam = data[2]
    if dsd == []:
        print("У студента", name, fam, "оценок нет")
        return
    for i in dsd:
        if i[1] == (lesson-1): j = i
    average = statistics.mean(j[2:])
    print("Средний балл студента по этому предмету", average)
    print()

# 3) Вывод среднего балла по школе по конкретному предмету
def average_rating(lesson):
    average = 0
    count = 0
    max = 0
    id_max = 0
    for i in dtp.data_lesson:
        if i[1] == lesson:
            sum1 = sum(i[2:])
            if sum1 > max:
                max = sum1
                id_max = i[0]
                j = i[2:]
            average1 = sum1 / (len(i[2:]))
            average += average1
            count += 1
    average = average / count
    print(f"Средний бал по школе для предмета {config.lesson_list[lesson-1]} =", round(average,2))
    print(f"Лучший студент по этому предмету", dtp.data_student[id_max-1], "  его оценки:", j)

# 4) Вывод количества учеников претендующих на золотую медаль (все оценки либо 4 либо 5)
def zoloto():
    zoloto = []
    for i in dtp.data_student:
        id = i[0]
        index = 1
        bal = 0
        summ = 0
        for j in dtp.data_lesson:
            if j[0] == id:
                summ1 = j[2] + j[3] + j[4] + j[5]
                if summ1 < 16: index = 0
                summ += summ1
        if index == 1: zoloto.append([i,summ])
    if zoloto == []: print("Золотых нет...")
    else:
        print()
        print("СПИСОК ЗОЛОТЫХ СТУДЕНТОВ:")
        for i in zoloto:
            print(i[0], "общий балл по оценкам:", i[1])