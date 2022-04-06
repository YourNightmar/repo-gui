# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 Two — 2 Three — 3 Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text_4.txt', 'r') as old_file:
    data = old_file.readlines()
    for i in data:
        i = i.split(' ', 1)
        new_file.append(translate[i[0]] + ' ' + i[1])

with open('text_4_new.txt', 'w') as new_file_1:
    new_file_1.writelines(new_file)
#проверка
with open('text_4_new.txt', 'r') as new_file_1:
    print(new_file_1.read())


#rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
#new_file = []
#with open('file_4.txt', 'r') as file_obj:
    #content = file_obj.read().split('\n')
#    for i in file_obj:
#        i = i.split(' ', 1)
#        new_file.append(rus[i[0]] + '  ' + i[1])
#   print(new_file)

#with open('file_4_new.txt', 'w') as file_obj_2:
#    file_obj_2.writelines(new_file)