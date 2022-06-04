def NegaFibonacci (num):
    lst = []
    for i in range (num * 2 + 1):
        lst.append(0)
    lst[num -1] = lst[num + 1] = 1
    for i in range (num - 1):
        lst[num + 2 + i] = lst[num + 1 + i] + lst[num + i]
        lst[num - 2 - i] = lst[num - i] - lst[num - 1 - i]
    return lst

num = int(input('Введите количество зеркальных элементов для Негафибоначчи: '))
nega_fib = NegaFibonacci (num)
print(nega_fib)