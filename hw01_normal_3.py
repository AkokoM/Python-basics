
__author__ = 'Kokorev Alexey Mihaylovich'

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

print('Вычесление корней квадратного уровнения вида ax² + bx + c = 0.')

a = float(input('Введите значение a = '))
b = float(input('Введите значение b = '))
c = float(input('Введите значение c = '))

# https://1cov-edu.ru/mat_analiz/funktsii/ratsionalnye/mnogochleny/kvadratnye-uravneniya/
# Рассмотрим дискриминант квадратного уравнения:
D = b ** 2 - 4 * a * c # Если дискриминант меньше нуля - корней нет. Если равен нулю - один корень. Если больше нуля - два корня.
if D > 0:
    x1 = ((-b - math.sqrt(D)) / (2 * a))
    x2 = ((-b + D ** .5) / (2 * a))
    print('x1 = %.2f' % x1)
    print('x2 = %.2f' % x2)
elif D == 0:
    x1 = (-b / (2 * a))
    print('x1 = %.2f' % x1)
elif D < 0:
    print('Нет действительных корней.')
else:
    pass