# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
xa = float(input('Введите координаты точки xa: '))
ya = float(input('Введите координаты точки ya: '))
xb = float(input('Введите координаты точки xb: '))
yb = float(input('Введите координаты точки yb: '))

distance = (((xb - xa) ** 2) + ((yb - ya) ** 2)) ** 0.5
print(round(distance, 2))
