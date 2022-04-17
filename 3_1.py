#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
#у пользователя, предусмотреть обработку ситуации деления на ноль.

#запрашиваю данные от пользователя
arg_1 = int(input('Enter first number: '))
arg_2 = int(input('Enter second number: '))
#создаю цикл для исключения деления на 0
while arg_2 != 0:
    def division(arg_1, arg_2):
        return arg_1 / arg_2
    print(division(arg_1, arg_2))
    break
else:
    print('Invalid function entered! Try again!')

#другой вариант
def division(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError as f:
        print(f'Error! Invalid function entered! Try again!')

print(division(int(input('Enter first number: ')), int(input('Enter second number: '))))