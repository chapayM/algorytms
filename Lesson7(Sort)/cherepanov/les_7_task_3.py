
__author__ = 'Черепанов Дмитрий Евгеньевич'

''' 3. Массив размером 2m + 1, где m — натуральное число, заполнен
случайным образом. Найдите в массиве медиану. Медианой называется
элемент ряда, делящий его на две равные части: в одной находятся
элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который
не рассматривался на уроках (сортировка слиянием также недопустима).'''

import random
from statistics import median


# Основное решение:
def find_median(array, k=None):
    n = len(array)
    if n == 1:
        return array[0]
    if k == None:
        k = n / 2
    pivot = array[random.randint(0, n - 1)]
    low_array = [item for item in array if item < pivot]
    high_array = [item for item in array if item > pivot]
    pivot_array = [item for item in array if item == pivot]
    if k < len(low_array):
        return find_median(low_array, k)
    elif k < len(low_array) + len(pivot_array):
        return pivot_array[0]
    else:
        return find_median(high_array, k - len(low_array) - len(pivot_array))


# Простое решение для проверки основного:
def find_median_sorted(array):
    half = len(array) // 2
    array.sort()
    return array[half]


m = 10
random_list = [random.randint(0, 49) for _ in range(2 * m + 1)]
print(f'Массив: {random_list}')
median_value = find_median(random_list)
print(f'Медиана: {median_value}')
print(f'Значение медианы для проверки (простое решение): {find_median_sorted(random_list)}')
print(f'Значение медианы для проверки: {median(random_list)}')
print(f'Отсортированный массив: {sorted(random_list)}')
