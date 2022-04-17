# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='utf-8') as file:
    low_income = []
    average_income = []
    my_l = file.read().split('\n')
    for i in my_l:
        i = i.split()
        if float(i[1]) <= 20000:
            low_income.append(i[0])
        average_income.append(i[1])
print(f'Income < 20000 {low_income}, average income - {sum(map(float, average_income)) / len(average_income)}')






#with open('sal.txt', 'r') as my_file:
    #sal = []
    #poor = []
    #my_list = my_file.read().split('\n')
    #for i in my_list:
    #    i = i.split()
    #    if int(i[1]) < 20000:
    #       poor.append(i[0])
    #    sal.append(i[1])
#print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')