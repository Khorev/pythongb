# Задание 2-1: Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_int = 5
my_float = 1.2
my_str = "Hello user"
my_list = ['a', '2']
my_tuple = ('b', '3')
my_dict = {'city': 'Ekaterinburg', 'country': 'Russia'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')
