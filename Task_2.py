# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# !=(X v Y v Z) - все элементы кроме, X, Y, Z
# != X ^ != Y ^ != Y - все что не объединяет X, Y, Z

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not (x) and not (y) and not (z)):
                print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно!')
