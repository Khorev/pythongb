# Задание 3-2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def my_func(name, surname, byear, city, email, phone):
    print(name, surname, byear, city, email, phone)

my_func(name='viacheslav', surname='khorev', byear=1976, city='Ekaterinburg', email='email', phone='6462')