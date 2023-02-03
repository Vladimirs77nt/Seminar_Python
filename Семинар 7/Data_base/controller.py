import config
import interface
import view
import data_processing as dtp

def controller():
    print ("запуск Controller")

    while True:
        n = interface.interf()

        if n == "0": break

        if n == "1":                      # 1 - показать базу данных (полностью)
            data_str = dtp.load(config.file_name)
            data = dtp.create_data(data_str)
            view.print_data(data)

        if n == "2":                      # 2 - показать базу данных (Имя и Фамилия)
            data_str = dtp.load(config.file_name)
            data = dtp.create_data(data_str)
            view.print_data_low(data)

        if n == "3":                      # 3 - сортировать справочник по ID
            data = dtp.sort_data_ID(data)
            print("- Сортировка по ID")
            view.print_data(data)
            dtp.save(data, config.file_name)

        if n == "4":                      # 4 - сортировать справочник по имени
            data = dtp.sort_data_Name(data)
            print("- Сортировка по Имени")
            view.print_data(data)
            dtp.save(data, config.file_name)

        if n == "5":                      # 5 - ввести новую запись
            dtnew = interface.input_new_data()
            data.append(dtnew)
            print("- Добавлена новая запись")
            view.print_data(data)
            dtp.save(data, config.file_name)

        if n == "6":                      # 6 - удаление записи по ID
            interface.delete_id()