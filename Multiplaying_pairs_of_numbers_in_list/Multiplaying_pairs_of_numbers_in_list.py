#from ast import Mult
import Create_list_random_int_from_0_to_9 as create
from math import ceil


def Multiplaying_pairs_of_numbers_in_list (any_list):
    new_list = []
    for item in range (ceil(len(any_list) / 2)):
        new_list.append(any_list[item] * any_list[len(any_list) - 1 - item])
    return new_list

length = int(input('Введите количество элементов в списке: '))
my_list = create.Create_list_random_int_from_0_to_9(length)
print(my_list)
new_list = Multiplaying_pairs_of_numbers_in_list(my_list)
print(new_list)