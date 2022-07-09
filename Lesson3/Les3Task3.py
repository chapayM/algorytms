# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint


# def max_min_change(array):
#     sort_array = sorted(array.copy())
#     index_min, index_max = array.index(sort_array[0]), array.index(sort_array[-1])
#     array[index_min], array[index_max] = sort_array[-1], sort_array[0]
#     sort_array.clear()
#     return array
def max_min_change(array):
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
    array[index_min], array[index_max] = max_el, min_el
    return array


list1 = [randint(0, 100) for _ in range(10)]
print(list1)
print(max_min_change(list1))
