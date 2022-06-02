from random import random

def Create_list_with_positive_real_nums(length, max):
    new_list = []
    for i in range (length):
        new_list.append(round(random() * max, 2))
    return new_list

def Fractional_part (real_number_list):
    fractional_parts_list = []
    for item in real_number_list:
        fractional_parts_list.append(item - int(item))
        fractional_parts_list[-1] = round(fractional_parts_list[-1], 2)
    return fractional_parts_list

def Diff_between_max_min (any_list):
    max = any_list[0]
    min = any_list[0]
    for i in range (1, len(any_list)):
        if any_list[i] > max:
            max = any_list[i]
        if any_list[i] < min:
            min = any_list[i]
    diff = max - min
    return diff

length = int(input('Введите количество элементов: '))
max = int(input('Введите максимальное значение элемента: '))
my_list = Create_list_with_positive_real_nums(length, max)
print(my_list)

my_list = Fractional_part(my_list)

diff = Diff_between_max_min(my_list)
print(f'Разница между максимальным и минимальным значеним дробной части элементов равна {diff}')