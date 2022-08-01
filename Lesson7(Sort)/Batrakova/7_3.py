#3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

m = int(input('Введите m: '))

list_1 = [i for i in range(1, 10)]
print('Исходный массив:')
print(list_1)

for j in range(m + 1):
    min = list_1[0]
    for i in range(0, len(list_1)):
        if list_1[i] < min:
            min = list_1[i]
    list_1.remove(min)
    print(list_1)

print('Медиана списка:')
print(min)
