# Задача
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

## Пример
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# Решение
Программа состоит из трех методов.
+ Создание и заполнение списка положительными действительными числами от 0 до `max`, аргумента, который вводится пользователем.
+ Заполнение нового массива дробными частями чисел из изначального массива с помощью вычитания из чисел их целой части с использованием метода `int`. И из-за отклонениях в вычислении _Python_ дальнейшее округления с помощью `round` до двух значащих цифр после запятой.
+ Нахождение в цикле минимального и максимального значения одновременно, чтобы не создавать два цикла. И вычисление разницы между ними.