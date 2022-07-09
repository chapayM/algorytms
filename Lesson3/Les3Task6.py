# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint


def sum_between_max_min(array):
    # sort_array = sorted(array.copy())
    # index_min, index_max = array.index(sort_array[0]), array.index(sort_array[-1])
    # sort_array.clear()
    max_el = array[0]
    min_el = array[0]
    i = 0
    while i < len(array) - 1:
        if max_el < array[i + 1]:
            max_el = array[i + 1]
        if min_el > array[i + 1]:
            min_el = array[i + 1]
        i += 1
    index_min, index_max = array.index(min_el), array.index(max_el)
    sum_res = 0
    if index_min < index_max:
        for el in array[index_min + 1:index_max]:
            sum_res += el
    else:
        for el in array[index_max + 1:index_min]:
            sum_res += el
    return sum_res


list1 = [randint(0, 100) for _ in range(10)]
print(list1)
print(sum_between_max_min(list1))
