import config
import data_processing as dtp
import controller
import view

def interf():
    d = ["0","1","2","3","4","5","6","7","8","9","100"]
    while True:
        print()
        print("Информационная система учеников школы")
        print("*** с журналом оценок за каждую четверть ***")
        print()
        print("Действия:")
        print("1 - показать список учеников")
        print("2 - добавить ученика")
        print("3 - показать список учебных предметов")
        print("4 - добавить новый учебный предмет")
        print("5 - показать оценки по ВСЕМ предметам для конкретного ученика")
        print("6 - добавить оценки по предмету для конкретного ученика")
        print("7 - вывод средней оценки ученика по одному предмету")
        print("8 - вывод среднего балла по школе по конкретному предмету")
        print("9 - вывод количества учеников претендующих на золотую медаль (все оценки либо 4 либо 5)")
        print("100 - генерация 100 случайных учеников")
        print("0 - завершение работы")
        n = input("* выберите действие: ")
        if n in d: break
        print("\n" * 10)
        print("*** неверный ввод данных! ***")
        print("повторите:")
    return n

def add_student():
    print("Добавление нового студента: ")
    name = input("Введите Имя студента: ")
    fam = input("Введите Фамилию студента: ")
    id = len(dtp.data_student) + 1
    data_line = [id, name, fam]
    print("новая запись: ", data_line)
    dtp.data_student.append(data_line)
    for indx, item in enumerate(config.lesson_list):
            est = [id, indx, 0, 0, 0, 0]
            dtp.data_lesson.append(est)
    dtp.save_lesson(dtp.data_lesson)
    dtp.load_lesson()
    view.print_diary(id)
    print()

def add_lesson():
    print("Добавление нового учебного предмета: ")
    name = input("Введите название учебного предмета: ")
    config.lesson_list.append(name)
    print("--- добавлен ---")
    print()

# def check_student(id):
#     print("Показ журнала оценок ")
#     print("Добавление нового учебного предмета: ")
#     name = input("Введите название учебного предмета: ")
#     config.lesson_list.append(name)
#     print("--- добавлен ---")
#     print()