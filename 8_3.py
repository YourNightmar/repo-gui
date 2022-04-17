# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами
# выводится на экран.

class Task_exception(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

if __name__ == '__main__':
    my_list = []

    while True:
        user_input = input("Введите число для заполнения списка, или 'stop' для выхода: ")

        if user_input == "stop":
            break

        try:
            if not user_input.isdigit():
                raise Task_exception(f"'{user_input}' has not numerical format")

            my_list.append(int(user_input))
        except Task_exception as e:
            print(e)

    print(my_list)


