# Задание 4-4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from itertools import permutations
from itertools import repeat
from itertools import combinations
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [el for el in my_list if my_list.count(el)==1]
print(new)