# Задание 5-2. Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

my_list = ['Odin\n', 'Dva\n', 'Vosem\n']
with open("lesson 5-2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("lesson 5-2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")
