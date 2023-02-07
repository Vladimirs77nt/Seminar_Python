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

print ("Введите комплексное число, вида (a + bj)")
print ("a и b - вещественные числа")
print ("Сначала введите (а), затем через пробел, (b):")
text = input()
num_text = text.split()
print(num_text)
if text.isdigit:
    num = list(map(float,text.split()))
    compl = complex(num[0], num[1])
    print(compl)