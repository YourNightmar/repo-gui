#запрос пользователя для ввода числа
num = int(input('Enter a number: '))
#расчет в формате чч:мм:сс
result_1 = num // 3600
result_2 = (num - (result_1 * 3600)) // 60
result_3 = (num - (result_1 * 3600) - (result_2 * 60)) % 60
#выводим результат
print(f'{result_1}:{result_2}:{result_3}')