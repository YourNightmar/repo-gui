#создаем запрос от человека
num = int(input('Enter a number: '))
#переводим число в строку
num_rule = str(num)
#складываем необходимые строки
num_1 = num_rule + num_rule
num_2 = num_rule + num_rule + num_rule
#выводим результат с переводом в целочисленные выражение
print(num +int(num_1) + int(num_2))

