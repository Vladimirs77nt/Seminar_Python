import random
import telebot
from telebot import types
# pyTelegramBotAPI 4.9.0
# https://pypi.org/project/pyTelegramBotAPI/
bot = telebot.TeleBot("5516433386:AAGIRNxLwMSR-UZTmoeu0fWlyIHVlCrpoN4")

# КОМАНДА - "/START"
# ИНИЦИАЛИЗАЦИЯ
@bot.message_handler(commands = ["start"])
def start(message):
    global igrok, conf, conf_igrok

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("/start")
    but2 = types.KeyboardButton("Завершить игру")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "Запуск игры КОНФЕТЫ", reply_markup=markup)

    print("Запуск сервера игры КОНФЕТЫ")
    bot.send_message(message.chat.id,"Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.")
    conf = 221 # начальное количество конфеn
    igrok = random.randint(1,2)
    text = "Первым играет игрок №" + str(igrok)
    bot.send_message(message.chat.id,text)
    conf_igrok = [0 ,0]
    text = "Игрок №" + str(igrok) + " - введи количество конфет которые ты возьмешь: "
    bot.send_message(message.chat.id,text)
    print("Первый ход игрока №", igrok)

# ФУНКЦИЯ - ВВОД ТЕКСТА
@bot.message_handler(content_types=["text"])
def controller(message):
    global igrok, conf, conf_igrok
    if message.text == "Завершить игру":
        print("Завершение работы")
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
    elif conf>0:
        if message.text.isdigit():
            num = int(message.text)
            print(num)
            if int(message.text) >0 and int(message.text)<29:
                conf -= num
                if conf <= 0:
                    bot.send_message(message.chat.id,"Победа!")
                    text = "Победил игрок №" + str(igrok)
                    bot.send_message(message.chat.id,text)
                    bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
                    print("Победа! Победил игрок №", igrok)
                    bot.send_message(message.chat.id,"Игра завершена. Перезапустите игру /start")
                    print("Игра завершена")
                    bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)
                else:
                    conf_igrok [igrok-1] += num
                    if igrok == 2: igrok = 1
                    else: igrok = 2
                    text = "На столе осталось " + str(conf) + " конфет"
                    bot.send_message(message.chat.id,text)
                    text = "Ход переходит игроку № " + str(igrok)
                    bot.send_message(message.chat.id,text)
                    text = "Игрок №" + str(igrok) + " - введи количество конфет которые ты возьмешь: "
                    bot.send_message(message.chat.id,text)
                    print("Переход хода к игроку №", igrok)
            else:
                bot.send_message(message.chat.id,"* неверно! нужно ввести число от 1 до 28")
                bot.send_message(message.chat.id,"введи количество конфет которые ты возьмешь:")
        else:
            bot.send_message(message.chat.id,"Вы ввели текст... Нужно ввести число! от 1 до 28")
            bot.send_message(message.chat.id,"введи количество конфет которые ты возьмешь:")
    else:
        bot.send_message(message.chat.id,"Игра завершена. Перезапустите игру /start")
        print("Игра завершена")
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id)

# ЗАПУСК ВЫПОЛНЕНИЯ ПРОГРАММЫ
print("*** ЗАПУСК СЕРВЕРА ***")
conf = 221
bot.infinity_polling()