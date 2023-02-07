from fractions import Fraction  # модуль для работы с рациональными числами
import cmath                    # модуль для работы с комплексными числами
import datetime                 # модуль времени

# print ("Введите рациональное число, вида (m/n)")
# print ("Сначала введите числитель (m - целое число), затем через пробел, знаменатель (n - действительное число):")
# text = input()
# if text.isdigit:
#     num = list(map(int,text.split()))
#     frac = Fraction(num[0], num[1])
#     print(frac)

# print ("Введите комплексное число, вида (a + bj)")
# print ("a и b - вещественные числа")
# print ("Сначала введите (а), затем через пробел, (b):")
# text = input()
# num_text = text.split()
# print(num_text)
# if text.isdigit:
#     num = list(map(float,text.split()))
#     compl = complex(num[0], num[1])
#     print(compl)


from fractions import Fraction  # модуль для работы с рациональными числами
import cmath        # модуль для работы с комплексными числами
import datetime     # модуль времени
import telebot      # модуль для работы ботом в Telegram
from telebot import types

bot = telebot.TeleBot("5516433386:AAGIRNxLwMSR-UZTmoeu0fWlyIHVlCrpoN4")

@bot.message_handler(content_types=["text"])
def controller (message):
    print(message.from_user.username)
    print(message.from_user.first_name + " " + message.from_user.last_name)

# ЗАПУСК ВЫПОЛНЕНИЯ ПРОГРАММЫ
print("*** ЗАПУСК СЕРВЕРА ***")
bot.infinity_polling()