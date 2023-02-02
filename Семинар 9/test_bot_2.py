import telebot
from telebot import types
# pyTelegramBotAPI 4.9.0
# https://pypi.org/project/pyTelegramBotAPI/

bot = telebot.TeleBot("5516433386:AAGIRNxLwMSR-UZTmoeu0fWlyIHVlCrpoN4")
count = 0

# ФУНКЦИЯ - СУММА
def summa(message):
    print("* кнопка Сумма")
    summ = sum(list(map(int,message.text.split())))
    bot.send_message(message.chat.id, str(summ))
    button(message)

# ФУНКЦИЯ - РАЗНОСТЬ
def raznost(message):
    print("* кнопка Разность")
    num = list(map(int,message.text.split()))
    diff = num[0] - num[1]
    bot.send_message(message.chat.id, str(diff))
    button(message)

# КОМАНДА - "/START"
@bot.message_handler(commands = ["start"])
def start(message):
    global count
    count += 1
    print(count)
    print("запуск def: start")
    bot.send_message(message.chat.id,f"/button")
    print("завершение def: start")

# КОМАНДА - "/BUTTON"
@bot.message_handler(commands = ["button"])
def button(message):
    global count
    count += 1
    print(count)
    print("запуск def: button")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("сумма")
    but2 = types.KeyboardButton("разность")
    markup.add(but1)
    markup.add(but2)
    print("* кнопки добавлены")
    bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)
    print("завершение def: button")

# ФУНКЦИЯ - ПРИЕМ ВВЕДЕНОГО СООБЩЕНИЯ
@bot.message_handler(content_types=["text"])
def controller(message):
    global count
    count += 1
    print(count)
    print("запуск def: text")
    if message.text == "сумма":
        bot.send_message(message.chat.id,"введи два числа для их суммы: ")
        bot.register_next_step_handler(message, summa)
    if message.text == "разность":
        bot.send_message(message.chat.id,"введи два числа для их разности: ")
        bot.register_next_step_handler(message, raznost)
    print("завершение def: text")

# ЗАПУСК ВЫПОЛНЕНИЯ ПРОГРАММЫ
print("*** ЗАПУСК СЕРВЕРА ***")
bot.infinity_polling()