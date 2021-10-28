import math


print("{:.1f}".format(math.e))
print("{:.2f}".format(math.pi))


x1 = x2 = x3 = v0 = m1 = m2 = 1
t = a = m = v = g = h = b = c = y = r = d = x = 1
R1 = R2 = L = R = I = 1

lab3_2a = math.sqrt(x1**2 + x2**2)
lab3_2b = x1 * x2 + x1 * x3 + x2 * x3
lab3_2c = v0 * t + (a * t**2) / 2
lab3_2d = m * v**2 / 2 + m * g * h
lab3_2e = 1 / R1 + 1 / R2
lab3_2f = m * g * math.cos(L)
lab3_2g = 2 * math.pi * R
lab3_2h = b**2 - 4 * a * c
lab3_2i = y * m1 * m2 / r**2
lab3_2j = I**2 * R
lab3_2k = a * b * math.sin(c)
lab3_2l = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(c))
lab3_2m = (a * d + b * c) / (a * d)
lab3_2n = math.sqrt(1 / math.sin(x)**2)
lab3_2o = 1 / math.sqrt(a * x**2 + b * x + c)
lab3_2p = (math.sqrt(x + 1) + math.sqrt(x - 1)) / (2 * math.sqrt(x))
lab3_2q = abs(x) + abs(x + 1)
lab3_2r = abs(1 - abs(x))


def lab3_3(x, y):
    z = x**3 - 2.5 * x * y + 1.78 * x**2 - 2.5 * y + 1
    return z


def lab3_4(a, b):
    '''Функция вычисляет периметр прямоугольного треугольника по значениям 2-х катетов'''
    c = a**2 + b**2
    return a + b + math.sqrt(c)


print(lab3_3(x, y))

a, b = list(map(int, input("Пользователь, введите значения катетов a и b прямоугольного треугольника: ").split()))
print(f"Периметр прямоугольного треугольника с катетами {a} и {b} равен {lab3_4(a, b)}")