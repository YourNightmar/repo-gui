# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
# использую файл text_7.txt из архива к ДЗ.
def count_info():
    try:
        with open('text_7.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            for i in range(len(my_list)):
                new_list = my_list[i].split()
                print(f'Количество строк в файле {len(my_list)}. В {i + 1}-ой строке {len(new_list)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'

print(count_info())