# Задача 8-3. Создайте собственный класс-исключение, который должен проверять содержимое списка
# на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду stop.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и
# вносить его в список, только если введено число. Класс-исключение должен
# не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class NaNError(Exception):
    def __init__(self, txt):
        self.txt = txt


def number_filter(string):
    if string.isdigit():
        return string
    else:
        try:
            float(string)
            return string
        except ValueError:
            raise NaNError(f'Error: {string} - is not a number')


input_txt = ''
counter = 1
numbers_list = []
print("Введите числа по одному, для выхода введите 'stop'")
while input_txt != 'stop':
    try:
        input_txt = input(f"{counter}: ")
        numbers_list.append(number_filter(input_txt))
        counter += 1
    except NaNError as e:
        if input_txt != 'stop':
            print(e.txt)

print(f"Result list:\n{numbers_list}")