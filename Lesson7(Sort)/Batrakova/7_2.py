# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

list_1 = [random.uniform(0, 50) for i in range(10)]
print(list_1)

import operator
def merge_sort(list, compare=operator.lt):
    if len(list) < 2:
        return list[:]
    else:
        middle = int(len(list) / 2)
        left = merge_sort(list[:middle], compare)
        right = merge_sort(list[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

print(merge_sort(list_1))