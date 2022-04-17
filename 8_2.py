# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class My_err:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    @staticmethod
    def delenie(param_1, param_2):
        try:
            return param_1 / param_2
        except:
            if param_2 == 0:
                return f'Деление на ноль недопустимо'


param_1 = int(input('Введите число: '))
param_2 = int(input('Введите еще одно число: '))
delen = My_err.delenie(param_1, param_2)
print(delen)