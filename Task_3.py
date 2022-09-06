# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите абсциссу: '))
y = int(input('Введите ординату: '))

if x != 0 and y != 0:
    if x < 0:
        if y < 0:
            print('3 четверть')
        else:
            print('2 четверть')
    else:
        if y < 0:
            print('4 четверть')
        else:
            print('1 четверть')
