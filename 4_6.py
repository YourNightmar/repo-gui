#Реализовать два небольших скрипта:
#итератор, генерирующий целые числа, начиная с указанного;
#итератор, повторяющий элементы некоторого списка, определённого заранее.
#Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание,
#что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
#Например,в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
#Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from itertools import count, cycle

num = int(input('Enter the number: '))

for i in count(num):
    if i > 25:
        break
    else:
        print(i)

i = 0
for b in cycle([1, 2, 3, 4, 5]):
    if i > 30:
        break
    print(b)
    i += 1