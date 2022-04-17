#создаю свой лист "рейтинг"
my_list = [9, 7, 7, 6, 3]

#запрашиваю от пользователя натуральное число
num = int(input('Enter natural number: '))
#узнаю количество повторяющихся элементов в списке равных запрошенному числу
a = my_list.count(num)
for el in my_list:
    if a > 0:
        i = my_list.index(num)
        my_list.insert(i + a, num)
        break
    else:
        if num > el:
            s = my_list.index(el)
            my_list.insert(0, num)
            break
        elif num < my_list[len(my_list) - 1]:
            my_list.append(num)
print(my_list)