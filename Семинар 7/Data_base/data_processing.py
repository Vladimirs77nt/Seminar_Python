import config

def save(data, name):
    dstr = ""
    for i in data:
        i[0] = str(i[0])
        for j in i:
            dstr = dstr + j + " "
        dstr = dstr + '\n'
    f = open(name, 'w')
    f.write(dstr)
    f.close()
    print("* файл записан")

def load(name):
    file = open(name, 'r')
    f = [i.rstrip() for i in file]
    t = []
    for item in f: t.append(str(item))
    file.close()
    print("* файл прочитан")
    return t

def create_data(data_str):
    dt = [i.split() for i in data_str]
    for i in dt: i[0] = int(i[0])
    return dt

# def create_data_str(data):
#     for i in dt: i[0] = int(i[0])
#     return dt

def sort_data_ID(data):
    dts = sorted(data, key = lambda x: int(x[0]))
    return dts

def sort_data_Name(data):
    dts = sorted(data, key = lambda x: x[2])
    return dts