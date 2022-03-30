#Выполнить функцию, которая принимает несколько параметров, описывающих данные
#пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
#должна принимать параметры как именованные аргументы. Осуществить вывод данных о
#пользователе одной строкой.

def human_data(name, surname, birthyear, city, email, phone):
    return print(f' Name: {name} Surname: {surname} Birthyear: {birthyear} City: {city} Email: {email} Phone: {phone}')

human_data(name=input('Name: '), surname=input('Surname: '), birthyear=input('Birthyear: '),
    city=input('City: '), email=input('Email: '), phone=input('Phone: '))