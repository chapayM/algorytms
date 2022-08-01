
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 2. Отсортируйте по возрастанию методом слияния одномерный вещественный
массив, заданный случайными числами на промежутке [0; 50). Выведите на
экран исходный и отсортированный массивы.'''

import random


def merge_sort(array):
    na = len(array)
    if na <= 1:
        return array
    left_part = merge_sort(array[:na // 2])
    right_part = merge_sort(array[na // 2:])
    n, m, k = 0, 0, 0
    sorted_array = [0] * (len(left_part) + len(right_part))
    while n < len(left_part) and m < len(right_part):
        if left_part[n] <= right_part[m]:
            sorted_array[k] = left_part[n]
            n += 1
        else:
            sorted_array[k] = right_part[m]
            m += 1
        k += 1
    while n < len(left_part):
        sorted_array[k] = left_part[n]
        n += 1
        k += 1
    while m < len(right_part):
        sorted_array[k] = right_part[m]
        m += 1
        k += 1   
    return sorted_array
    


random_list = [random.randint(0, 49) for _ in range(10)]
print(f'Исходный массив: {random_list}')
sorted_list = merge_sort(random_list)
print(f'Отсортированный массив: {sorted_list}')
