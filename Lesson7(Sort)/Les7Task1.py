# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random

# array = [i for i in range(-100, 100)]
# random.shuffle(array)
array = [91, -88, -87, -93, -1, 99, 15, -38, 73, 45]
print(array)


def bubble_sort(array):
    count = 0
    n = 1
    swap = True  # контролируем, что на каком-то циклие измененние в списке не произошло и тогда завершаем сортировку.
    while n < len(array) and swap == True:
        swap = False
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
            count += 1
        n += 1
    print(count)


bubble_sort(array)
print(array)
