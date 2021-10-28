def lab1_1(a):
    '''Функция вычисляет значение x и y при известном a'''
    x = 12 * a**2 - 16
    y = 7 * x**2 -3 * x + 6
    return x, y


def lab1_2(a, b):
    '''Функция вычисляет периметр и площадь четырехугольника со сторонами a и b'''
    p = 2 * (a + b)
    s = a * b
    return p, s


def degrees(num):
    '''Функция возвращает соответствующую форму слова градус для числа'''
    if num % 10 == 0 or 5 <= num % 100 <= 20 or 5 <= num % 10 <= 9:
        return "градусов"
    elif 2 <= num % 10 <= 4:
        return "градуса"
    else:
        return "градус"


class Degree():
    def __init__(self, celsius):
        self.celsius = celsius

    def getCelsius(self):
        return self.celsius

    def getFahrenheit(self):
        return self.celsius * 1.8 + 32

    def getKelvin(self):
        return self.celsius + 273.15

a = float()
xy = lab1_1(a)
print(f"При а равном {a}, x = {xy[0]:.2f}, y = {xy[1]:.2f}")

b = float()
ps = lab1_2(a, b)
print(f"Для четырехугольника со сторонами {a} и {b}, периметр = {ps[0]:.2f}, площадь = {ps[1]:.2f}")

degree = Degree(36.6)
print(f"{degree.getCelsius():.2f} {degrees(degree.getCelsius())} по Цельсию это " \
      f"{degree.getFahrenheit():.2f} {degrees(degree.getFahrenheit())} по Фаренгейту или " \
      f"{degree.getKelvin():.2f} {degrees(degree.getKelvin())} по Кельвину")
