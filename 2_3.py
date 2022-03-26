#делаю запрос пользователю ввести месяц в числовом эквиваленте
month = int(input('Enter number of month from 1 to 12: '))
#создаю список и словарь для определения времен года
month_list = ['winter', 'spring', 'summer', 'autumn']
month_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
#формирую условия отбора месяца к подходящему времени года для словаря и листа
if month == 12 or month == 1 or month == 2:
    print('Season is ' + month_list[0])
    print('Season is ' + month_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print('Season is ' + month_list[1])
    print('Season is ' + month_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print('Season is ' + month_list[2])
    print('Season is ' + month_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print('Season is ' + month_list[3])
    print('Season is ' + month_dict.get(4))
else:
    print('Incorrect data has been entered. Try again!')


