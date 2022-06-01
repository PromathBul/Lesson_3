from random import randint

def Create_list_random_int_from_0_to_9 (length):
    random_list = []
    for item in range(length):
        random_list.append(randint(0, 9))
    return random_list

def Sum_of_elements_on_odd_positions(any_list):
    sum = 0
    for i in range(len(any_list)):
        if i % 2 != 0:
            sum += any_list[i]         
    return sum
length = int(input('Введите количество элементов списка: '))
my_list = Create_list_random_int_from_0_to_9(length)
print(my_list)
sum = Sum_of_elements_on_odd_positions(my_list)
print(f'Cумма элементов, находящихся на нечетных позициях равна {sum}')