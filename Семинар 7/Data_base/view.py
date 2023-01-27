import config

def print_data(data):
    print("-"*82)
    print("|   ID   |   Фамилия    |     Имя      |       телефон      |    комментарий     |")
    print("-"*82)
    for i in data: print("|{0:^8}|{1:^14}|{2:^14}|{3:^20}|{4:^20}|".format(i[0], i[1], i[2], i[3], i[4]))
    print("-"*82)

def print_data_low(data):
    print("-"*31)
    print("|   Фамилия    |     Имя      |")
    print("-"*31)
    for i in data: print("|{0:^14}|{1:^14}|".format(i[1], i[2]))
    print("-"*31)