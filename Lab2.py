def input_2_number(some_input):
    '''Функция пытается перевести строку в int или float'''
    try:
        some_input = int(some_input)
    except ValueError:
        try:
            some_input = float(some_input)
        except ValueError:
            some_input = None
    finally:
        return some_input


def lab2_1(some_input):
    some_input = input_2_number(some_input)
    if some_input:
        print(f"Вы ввели число: {some_input}")
    else:
        print("Что-то пошло не так. Ожидались значения типа int() или float()")


def lab2_2(some_input):
    some_input = input_2_number(some_input)
    if some_input:
        print(f"{some_input} - вот какое число Вы ввели")
    else:
        print("Что-то пошло не так. Ожидались значения типа int() или float()")


lab2_1(input("Пользователь, введите число: "))

lab2_2(input("Пользователь, введите число: "))

print(1, 13, 49)

print(50, 10, sep='\n')

x, y = list(map(int, input("Пользователь, введите значения x и y через пробел: ").split()))
print("а) 7 см\n"
      f"б) {x} 25\n"
      f"в) {x} {y}")
