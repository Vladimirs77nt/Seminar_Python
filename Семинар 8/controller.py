import config
import interface
import view
import data_processing as dtp

def start():
    print ("запуск Controller")
    
    dtp.init()

    while True:
        n = interface.interf()

        if n == "0": break

        if n == "1":                      # 1 - показать список учеников"
            view.print_student(dtp.data_student)
            input("Нажмите клавишку Enter...")
            print()

        if n == "2":                      # 2 - добавить ученика
            interface.add_student()
            dtp.save_student(dtp.data_student)
            print()

        if n == "3":                      # 3 - показать список учебных предметов
            view.print_lesson()
            input("Нажмите клавишку Enter...")
            print()

        if n == "4":                      # 4 - добавить новый учебный предмет
            interface.add_lesson()

        if n == "5":                      # 5 - ПОКАЗАТЬ оценки по всем предметам для конкретного ученика
            id = int(input("Введите ID студента: "))
            dsd = dtp.student_diary(id)
            index = dtp.index_ID
            name = dtp.id_name
            fam = dtp.id_fam
            if index < 0:
                print("Такого студента нет!")
            elif dsd == []:
                print("Для студента", name, fam, " - оценок нет")
            else:
                view.print_diary(id)
            input("Нажмите клавишку Enter...")
            print()

        if n == "6":                      # 6 - добавить оценки по предмету для конкретного ученика
            dtp.add_estimation()
            input("Нажмите клавишку Enter...")
            print()

        if n == "7":                      # 7 - вывод средней оценки ученика по одному предмету
            id = int(input("Введите ID студента: "))
            view.print_lesson()
            lesson = int(input("Введите номер предмета: "))
            view.print_average(id, lesson)
            input("Нажмите клавишку Enter...")
            print()

        if n == "8":                      # 8 - вывод среднего балла по школе по конкретному предмету
            view.print_lesson()
            lesson = int(input("Введите номер предмета: "))
            view.average_rating(lesson)
            input("Нажмите клавишку Enter...")
            print()

        if n == "9":   # 9 - вывод количества учеников претендующих на золотую медаль (все оценки либо 4 либо 5)
            view.zoloto()
            input("Нажмите клавишку Enter...")
            print()

        if n == "100":                      # 100 - генератор журнала студентов и оценок
            # num = int(input("Введите количество студентов: "))
            dsd = dtp.generator_student(100)