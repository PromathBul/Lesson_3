def Dec_to_bin (number):
    txt_bin = ''
    while number > 0:
        txt_bin = str(number % 2) + txt_bin
        number //= 2
    return txt_bin

number = int(input('Введите число: '))
bin_number = Dec_to_bin(number)
print(bin_number)