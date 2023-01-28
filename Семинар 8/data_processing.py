import random
import config
import controller
import view

def init():
    load_student()
    print("* файл STUDENT прочитан")
    load_lesson()
    print("* файл LESSON прочитан")

def load_student(): # Чтение файла Student_ID.txt - список студентов
    file = open(config.file_name_student_ID, 'r')
    f = [i.rstrip() for i in file]
    t = []
    for item in f: t.append(str(item))
    file.close()
    ds = [i.split() for i in t]
    for i in ds: i[0] = int(i[0])
    global data_student
    data_student = list(ds) # data_student

def save_student(data): # Запись файла Student_ID.txt - список студентов
    dstr = ""
    for i in data:
        for j in i: dstr = dstr + str(j) + " "
        dstr = dstr[:-1]
        dstr = dstr + '\n'
    dstr = dstr[:-1]
    f = open(config.file_name_student_ID, 'w')
    f.write(dstr)
    f.close()
    print("--- файл Student_ID.txt обновлен ---")

def load_lesson(): # Чтение файла Lesson_ID.txt - журнал оценок по предметам
    file = open(config.file_name_lesson, 'r')
    f = [i.rstrip() for i in file]
    t = []
    for item in f: t.append(str(item))
    file.close()
    global dl
    dl = [i.split() for i in t]
    for indx, elem in enumerate(dl):
        dl[indx] = list(map(int, elem))
    global data_lesson
    data_lesson = list(dl) # data_lesson

def save_lesson(data): # Запись файла Lesson_ID.txt - список студентов
    dstr = ""
    for i in data:
        for j in i: dstr = dstr + str(j) + " "
        dstr = dstr[:-1]
        dstr = dstr + '\n'
    dstr = dstr[:-1]
    f = open(config.file_name_lesson, 'w')
    f.write(dstr)
    f.close()
    print("--- файл Lesson_ID.txt обновлен ---")

def student_diary(id_student): # Создание дневника студента
    global index_ID   # индекс записи о студенте в data_student
    index_ID = -1
    for indx, item in enumerate(data_student):
        if item[0] == id_student: index_ID = indx
    if index_ID < 0: return
    global data_student_diary
    data_student_diary = []
    for i in dl:
        if i[0] == id_student: data_student_diary.append(i[:])
    student = data_student[index_ID]
    global id_name, id_fam
    id_name = student[1]
    id_fam = student[2]
    return data_student_diary

def load_ID(name):
    file = open(name, 'r')
    f = [i.rstrip() for i in file]
    t = []
    for item in f: t.append(str(item))
    file.close()
    print("* файл прочитан")
    return t

# 1) Добавить функцию генерации сразу ста учеников и записи их в журнал
def generator_student(num):
    data = []
    lesson = []
    for i in range(num):
        id = i+1
        random_name = config.name_list[random.randint(0, len(config.name_list) - 1)]
        random_fam = config.fam_list[random.randint(0, len(config.fam_list) - 1)]
        d1 = [id, random_name, random_fam]
        data.append(d1)
        for indx, item in enumerate(config.lesson_list):
            n1 = random.randint(3,5)
            n2 = random.randint(3,5)
            n3 = random.randint(3,5)
            n4 = random.randint(3,5)
            les1 = [id, indx, n1, n2, n3, n4]
            lesson.append(les1)
    save_student(data)
    save_lesson(lesson)
    init()

def add_estimation():
    id = int(input("Введите ID студента: "))
    view.print_lesson()
    lesson = int(input("Введите номер предмета: "))
    estimation = input("Введите 4 оценки (1-5) за каждую четверть (через пробел): ")
    estimation = estimation.split()
    estimation = list (map(int, estimation))
    for indx, item in enumerate(data_lesson):
        if item[0] == id and item[1] == (lesson-1):
            est = [id, (lesson-1)] + estimation
            data_lesson[indx] = est
            print("запись оценок сделана")
    save_lesson(data_lesson)
    load_lesson()