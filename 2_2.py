#запрос данных от пользователя

my_int = int(input('Enter the integer number: '))
my_float = float(input('Enter the float number: '))
my_bool = bool(input('Enter the bool meaning: '))
my_str = str(input('Enter the string: '))
my_list = list(input('Enter the list: '))
my_tuple = tuple(input('Enter the tuple: '))

#формирую основной лист
head_list = [my_int, my_float, my_bool, my_str, my_list, my_tuple]
print(head_list)
#изменяю положение соседних объектов
#для четного списка
if len(head_list) % 2 == 0:
#начинаем слева направо
    i = 0
    while i < len(head_list):
#вношу переменные и их движение в условие цикла
        el = head_list[i]
        head_list[i] = head_list[i + 1]
        head_list[i + 1] = el
#следующая итерация через пару элементов списка
        i += 2
#для нечетного списка
else:
    i = 0
    while i < len(head_list) - 1:
        el = head_list[i]
        head_list[i] = head_list[i + 1]
        head_list[i + 1] = el
        i += 2
print(head_list)
