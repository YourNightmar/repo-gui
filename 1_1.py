#создаем запрос пользователю о выборе действия
act = input('Select an action (+,-,*,/): ')
#создаем запрос пользователю о выборе числа
num_1 = int(input('Enter a number: '))
num_2 = int(input('Enter a number: '))

if act == '+':
    result = num_1 + num_2
    print(result)
elif act == '-':
    result = num_1 - num_2
    print(result)
elif act == '*':
    result = num_1 * num_2
    print(result)
elif act == '/':
    result = num_1 / num_2
    print(result)
else:
    print('Invalid command entered, repeat the request!')