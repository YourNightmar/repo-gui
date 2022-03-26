#ввожу данные согласно задания

my_int = 436
my_float = 73.9
my_bool = True
my_str = 'Дорогу осилит идущий'
my_list = ['g', 23, False]
my_tuple = (2, 78)
my_dict = {1: 'Вверх', 2: 'Вправо', 3: 'Вниз', 4: 'Влево'}

#формирую основной лист
head_list = [my_int, my_float, my_bool, my_str, my_list, my_tuple, my_dict]

#формирую ответ по типу данных при помощи цикла for in
for i in head_list:
    print(f'{i} is {type(i)}')