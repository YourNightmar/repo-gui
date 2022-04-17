#Реализовать функцию my_func(), которая принимает три позиционных аргумента и
#возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    print(f'The sum of the two largest arguments: {arg_1 + arg_2 + arg_3 - min([arg_1, arg_2, arg_3])}')

my_func(int(input('Enter first argument: ')), int(input('Enter second argument: ')), int(input('Enter third argument: ')))