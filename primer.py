a = "23.567"
list_num = a.split(".")
print(list_num)
for i in range(len(list_num)):
    list_num[i] = int(list_num[i])
print(list_num)
