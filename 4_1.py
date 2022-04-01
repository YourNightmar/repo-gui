#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для
# конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script, output_in_hours, rate_per_hour, bonus = argv

def my_salary(output_in_hours, rate_per_hour, bonus):
    try:
        result = (int(output_in_hours) * float(rate_per_hour)) + int(bonus)
    except ValueError:
        return
    return result

print(f'{my_salary(output_in_hours, rate_per_hour, bonus)}')
