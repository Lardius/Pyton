#Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.

a = int(input('Введите первое число: '))
n = int(input('Введите разность (шаг): '))
d = int(input('Введите количество чисел: '))
for i in range(a, (a + (n*d)), n):
    print(i)

#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

list=[4, 9, 8, 1, 6, 2, 5, 9, 6, 7, 4, 1, 1, 5, 1, 2, 2, 2, 8, 2]
min_number = int(input())
max_number = int(input())
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)