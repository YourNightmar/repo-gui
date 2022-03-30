#Программа принимает действительное положительное число x и целое отрицательное число
#y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
#my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
#числа в степень.

def my_func(x, y):
    try:
        while y < 0:
            return (1 / x ** abs(y))

    except ZeroDivisionError as f:
        x = 0 and y < 0
        print(f'ZeroDivisionError! Try again!')

print(my_func(x=int(input('Enter valid positive X: ')), y=int(input('Enter negative Y: '))))

#Второй вариант.
def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1 / result

print(my_func(x=int(input('Enter valid positive X: ')), y=int(input('Enter negative Y: '))))