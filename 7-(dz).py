# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋁ - дизъюнкия / ИЛИ / OR
# ⋀ - конъюнкия / И / AND
# ¬ - инверсия

print()
print ("              левая часть  | правая часть уравнения")
print ("| X | Y | Z | ¬(X ⋁ Y ⋁ Z) | ¬X ⋀ ¬Y ⋀ ¬Z |")
for X in range (2):
    for Y in range (2):
        for Z in range (2):
            result1 = int(not (X or Y or Z))          # результат логических операций левой части уравнения
            result2 = int (not X and not Y and not Z) # результат логических операций правой части уравнения
            print ("|{0:^3}|{1:^3}|{2:^3}|{3:^14}|{4:^14}|".format(X, Y, Z, result1, result2),end="")
            if result1 == result2:
                print ("true")
            else:
                print ("false")
