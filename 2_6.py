#Создаю словарь Товары
goods = []
#запрашиваю от пользователя товары
while input('Вы хотите добавить товар? yes/no: ') == 'yes':
    num_good = int(input('Введите порядковый номер товара: '))
#заношу ключ и объект (характеристика и ее описание)
    characteristics = {}
    while input('Хотите ли вы добавить характеристику товара? yes/no: ') == 'yes':
        characteristic_key = input('Введите название характеристики: ')
        characteristic_definition = input('Введите описание характеристики: ')
        characteristics[characteristic_key] = characteristic_definition
#добавляю кортеж в товары по каждому товару
    goods.append(tuple([num_good, characteristics]))
print(goods)

analitics = {}
for good in goods:
    for characteristic_key, characteristic_definition in good[1].items():
        if characteristic_key in analitics:
            analitics[characteristic_key].append(characteristic_definition)
        else:
            analitics[characteristic_key] = [characteristic_definition]
print(analitics)