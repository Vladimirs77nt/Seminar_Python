import random
import telebot
from telebot import types
# pyTelegramBotAPI 4.9.0
# https://pypi.org/project/pyTelegramBotAPI/
bot = telebot.TeleBot("5516433386:AAGIRNxLwMSR-UZTmoeu0fWlyIHVlCrpoN4")

@bot.message_handler(commands = ["button", "start"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Старт игры - против другого игрока")
    but2 = types.KeyboardButton("Старт игры - против БОТА (глупый)")
    but3 = types.KeyboardButton("Старт игры - против БОТА (умный)")
    but4 = types.KeyboardButton("Завершить игру")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    bot.send_message(message.chat.id, "Запуск игры КОНФЕТЫ", reply_markup=markup)

# СТАРТ - ИГРА ПРОТИВ ЧЕЛОВЕКА
def start_human(message):
    global igrok, conf, conf_igrok, bot_igrok
    bot_igrok = 0
    print("Запуск сервера игры КОНФЕТЫ. Играют два игрока друг против друга (без бота)")
    bot.send_message(message.chat.id,"Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.")
    conf = 221   # начальное количество конфеn
    igrok = random.randint(1,2)
    text = "Первым играет игрок №" + str(igrok)
    bot.send_message(message.chat.id,text)
    conf_igrok = [0 ,0]
    text = "Игрок №" + str(igrok) + " - введи количество конфет которые ты возьмешь: "
    bot.send_message(message.chat.id,text)
    print("Первый ход игрока №", igrok)

# СТАРТ - БОТ
def start_bot(message):
    print("Старт игры - против БОТА")
    global igrok, conf, conf_igrok, bot_igrok
    print("Запуск сервера игры КОНФЕТЫ. Играет игрок №1 против БОТА (игрок №2)")
    bot.send_message(message.chat.id,"Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.")
    conf = 221   # начальное количество конфеn
    igrok = random.randint(1,2)
    text = "Первым играет игрок №" + str(igrok)
    bot.send_message(message.chat.id,text)
    conf_igrok = [0 ,0]
    text = "Игрок №" + str(igrok) + " - введи количество конфет которые ты возьмешь: "
    bot.send_message(message.chat.id,text)
    print("Первый ход игрока №", igrok)
    if igrok == 2:
        num = random.randint(1,28)
        text = "Бот взял " + str(num) + " конфет"
        bot.send_message(message.chat.id,text)
        conf -= num
        conf_igrok [igrok-1] += num
        igrok = 1
        text = "На столе осталось " + str(conf) + " конфет"
        bot.send_message(message.chat.id,text)
        bot.send_message(message.chat.id,"Ход переходит игроку № 1")
        bot.send_message(message.chat.id,"Игрок № 1 - введи количество конфет которые ты возьмешь: ")

# ПРОВЕРКА ПОБЕДЫ
def proverka_pobeda(message):
    global igrok, conf, conf_igrok, bot_igrok
    if conf <= 0:
        bot.send_message(message.chat.id,"Победа!")
        text = "Победил игрок №" + str(igrok)
        bot.send_message(message.chat.id,text)
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
        print("Победа! Победил игрок №", igrok)
        end_game(message)

# ХОД БОТА
    # bot_igrok = 1  -- ГЛУПЫЙ БОТ
    # bot_igrok = 2  -- УМНЫЙ БОТ
def hod_bot(message):
    global igrok, conf, conf_igrok, bot_igrok
    if bot_igrok == 1: num = random.randint(1,28)
    if bot_igrok == 2: num = (conf - (conf//28)*28)-1
    if num == 0: num = random.randint(1,28)
    if conf < 29: num = conf
    text = "Бот взял " + str(num) + " конфет"
    bot.send_message(message.chat.id,text)
    conf -= num
    proverka_pobeda(message)
    conf_igrok [igrok-1] += num
    igrok = 1
    if conf>0:
        text = "На столе осталось " + str(conf) + " конфет"
        bot.send_message(message.chat.id,text)
        bot.send_message(message.chat.id,"Ход переходит игроку № 1")
        bot.send_message(message.chat.id,"Игрок № 1 - введи количество конфет которые ты возьмешь: ")
        print("Ход переходит игроку № 1")

# ИГРА ЗАВЕРШЕНА
def end_game(message):
        bot.send_message(message.chat.id,"Игра завершена. Перезапустите игру /start")
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
        print("Игра завершена")

# ФУНКЦИЯ - ВВОД ТЕКСТА
@bot.message_handler(content_types=["text"])
def controller(message):
    global igrok, conf, conf_igrok, bot_igrok
    if message.text == "Старт игры - против БОТА (глупый)":
        bot_igrok = 1
        start_bot(message)
    if message.text == "Старт игры - против БОТА (умный)":
        bot_igrok = 2
        start_bot(message)
    elif message.text == "Старт игры - против другого игрока": start_human(message)
    elif message.text == "Завершить игру": end_game(message)
    elif conf>0:
        if message.text.isdigit():
            num = int(message.text)
            if int(message.text) >0 and int(message.text)<29:
                conf -= num
                proverka_pobeda(message)
                conf_igrok [igrok-1] += num
                if conf >0:
                    if igrok == 2: igrok = 1
                    else: igrok = 2
                    text = "На столе осталось " + str(conf) + " конфет"
                    bot.send_message(message.chat.id,text)
                    text = "Ход переходит игроку № " + str(igrok)
                    bot.send_message(message.chat.id,text)
                    text = "Игрок №" + str(igrok) + " - введи количество конфет которые ты возьмешь: "
                    bot.send_message(message.chat.id,text)
                    print("Переход хода к игроку №", igrok)
                    if bot_igrok >0 and igrok == 2: hod_bot(message)
            else:
                bot.send_message(message.chat.id,"* неверно! нужно ввести число от 1 до 28")
        else:
            bot.send_message(message.chat.id,"Вы ввели текст... Нужно ввести число! от 1 до 28")
    elif conf<1: end_game(message)


# ЗАПУСК ВЫПОЛНЕНИЯ ПРОГРАММЫ
print("*** ЗАПУСК СЕРВЕРА ***")
bot.infinity_polling()