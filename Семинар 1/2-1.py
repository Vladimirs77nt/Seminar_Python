num_max = Null
for i in range(5):
    num = int(input("Введите число {}: ".format(i+1)))
    if num_max<num:
        num_max = num
print ("Максимальное число: ", num_max)