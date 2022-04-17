# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('homework_5.txt', 'w') as file:
    file.write(input('Введите числа через пробел: '))
with open('homework_5.txt', 'r') as file_1:
    i = map(int, str(file_1.read()).split())
    print(sum(i))
