import random
import telebot
from telebot import types
bot = telebot.TeleBot("5516433386:AAGIRNxLwMSR-UZTmoeu0fWlyIHVlCrpoN4")

def summa(message):
    summ = sum(list(map(int,message.text.split())))
    bot.send_message(message.chat.id, str(summ))
    button(message)

def raznost(message):
    num = list(map(int,message.text.split()))
    diff = num[0] - num[1]
    bot.send_message(message.chat.id, str(diff))
    button(message)

@bot.message_handler(commands = ["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("сумма")
    but2 = types.KeyboardButton("разность")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def controller(message):
    if message.text == "сумма":
        bot.send_message(message.chat.id,"введи два числа для их суммы: ")
        bot.register_next_step_handler(message, summa)
    if message.text == "разность":
        bot.send_message(message.chat.id,"введи два числа для их разности: ")
        bot.register_next_step_handler(message, raznost)

bot.infinity_polling()


# conf = 221 # начальное количество конфет
# igrok = random.randint(1,2) 
# print ("Первым играет игрок №", igrok)
# conf_igrok = [0 ,0]

# while True:
#     print ("На столе лежит", conf, "конфет(а)")
#     while True:
#         print("Игрок", igrok, " - сколько возьмешь конфет? (от 0 до 28): ")
#         n = int(input())
#         if n>0 and n<29: break
#         print("- неверно указано кол-во конфет!")
#     if (conf-n) <= 0:
#         print("Победа!")
#         print("Победил игрок №", igrok)
#         break
#     conf_igrok [igrok-1] += n
#     conf -= n
#     if igrok == 2: igrok = 1
#     else: igrok = 2