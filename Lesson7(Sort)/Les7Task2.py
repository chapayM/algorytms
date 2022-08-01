# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


import random

array = [random.random() * 50 for i in range(0, 10)]
random.shuffle(array)
print(array)


def merge_sort(array):
    if len(array) <= 1:
        return array

    f_ar = merge_sort(array[:len(array) // 2])
    s_ar = merge_sort(array[len(array) // 2:])

    n = m = k = 0
    r_ar = [0] * (len(f_ar) + len(s_ar))
    while n < len(f_ar) and m < len(s_ar):
        if f_ar[n] <= s_ar[m]:
            r_ar[k] = f_ar[n]
            n += 1
        else:
            r_ar[k] = s_ar[m]
            m += 1
        k += 1
    while n < len(f_ar):
        r_ar[k] = f_ar[n]
        n += 1
        k += 1
    while m < len(s_ar):
        r_ar[k] = s_ar[m]
        m += 1
        k += 1
    for i in range(len(array)):
        array[i] = r_ar[i]
    return array


merge_sort(array)
print(merge_sort(array))
