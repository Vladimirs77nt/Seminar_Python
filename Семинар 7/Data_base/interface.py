import config
import data_processing

def interf():
    d = ["0","1","2","3","4","5","6"]
    while True:
        print("Телефонный справочник")
        print("Действия:")
        print("1 - показать базу данных (полностью)")
        print("2 - показать базу данных (Имя и Фамилия)")
        print("3 - сортировать справочник по ID")
        print("4 - сортировать справочник по имени")
        print("5 - ввести новую запись")
        print("6 - удалить запись по ID")
        print("0 - завершение работы")
        n = input("выберите действие: ")
        if n in d: break
        print("\n" * 10)
        print("*** неверный ввод данных! ***")
        print("повторите:")
    return n

def input_new_data():
    print("Ввод в справочник новой записи: ")
    id = int(input("Введите ID номер сотрудника: "))
    fam = input("Введите Фамилию сотрудника: ")
    name = input("Введите Имя сотрудника: ")
    tel = input("Введите номер телефона: ")
    comm = input("Введите дополнительный комментарий: ")
    data_line = [id, fam, name, tel, comm]
    print("новая запись: ", data_line)
    return data_line

def delete_id():
    print("- Удаление записи по ID")
    id = int(input("Введите ID номер сотрудника: "))
    print("- ЗАПИСЬ НЕ УДАЛЕНА. Модуль не доработан... ;-)")