#запрос пользователю на введение слов
my_str = input('Enter string: ')
a = my_str.split(' ')
#проверка разделения строки: print(a)
#формирую цикл
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[:10] #ограничиваю слово до 10 первых букв
    print(f'{i}). - {el}')
