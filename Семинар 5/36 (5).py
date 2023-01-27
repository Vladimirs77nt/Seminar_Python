# 36) Сделать с помощью filter, lambda
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Вывести все пробелы и их индексы из предыдущей строки.

# # А) МОЕ РЕШЕНИЕ
# text = "привет anc авф01абв авб абв02 123 primer --абв-- конец строки"
# print("Исходный текст:", text)
# f = "абв"

# text1 = text.split()
# text1 = list(filter(lambda x: x.find(f)<0, text1))
# text2 = ""
# l = int(len(text1))
# for i in range(l):
#     if i>0: text2 = text2 + " " + text1[i]
#     else: text2 = text2 + text1[i]
# print("Отфильтрованный текст:", text2)

# text2 = list(enumerate(text))
# text2 = list(filter(lambda x: x[1]==" ", text2))
# print(text2)

# Б) РЕШЕНИЕ ОТ АРТУРА
text = "ааабваа! аааа, аабв вввв. Абв ггг"
print(text)
text_list = text.split()
result = list(filter(lambda x: not "абв" in x.lower() ,text_list))
print(result)

for indx, val in enumerate(text):
    if val == " ": print (indx)