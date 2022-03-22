#создаем запрос спортсмену
a = int(input('Enter your first result: '))
b = int(input('Enter your desired result: '))
#задаю переменную день
day = 0
#создаю цикл пока желаемый результат не будет больше первого с учетом роста на 10%
while b - a >= 0:
    print(a, a * 1.1)
    a *= 1.1
    day += 1
print(str(day) + '. Good luck!')


