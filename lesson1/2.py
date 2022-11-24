# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

x = False
y = True
z = False


def logical(x, y, z):
    print((x or y or z) == (not(x) and not(y) and not(z)))


logical(x, y, z)
