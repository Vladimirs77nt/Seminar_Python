list_str = ["йцу", "фыв", "ячс", "цук", "йцукен"]
sub_str = "йцу"
count=0
for i in range(len(list_str)):
    if list_str[i] == sub_str:
        count += 1
    if count == 2:
        print(i)
        break
else:
    print(-1)
