#  Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#  Об окончании ввода данных будет свидетельствовать пустая строка.
lines = input('Enter the data: \n')
my_f = open('data.txt', 'w')
while lines:
    my_f.writelines(lines + '\n')
    lines = input('Введите текст \n')
    if not lines:
        break

my_f = open('data.txt', 'r')
information = my_f.read()
print(information)
my_f.close()

