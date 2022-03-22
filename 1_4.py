#создаем запрос пользователя для введения числа
num = int(input('Enter a positive number: '))

#создаю цикл по поиску максимального числа
max_num = num % 10
num = num // 10
while num > 0:
    if num % 10 > max_num:
        max_num = num % 10
    num = num // 10
print(max_num)
#попытался создать цикл по поиску минимального числа, не понимаю почему выдает 0?
min_num = num % 10
while num > 0:
    if num % 10 < min_num:
        min_num = num % 10
    num = num // 10
print(min_num)
