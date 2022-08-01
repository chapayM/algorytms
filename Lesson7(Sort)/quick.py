#<Быстрая сортировка Хоара (Сложность O(n^2) максимальная, до O(n log n).
# Неустойчивая. Тип - Обменная. Требует доп память - O(n)
import random

array = [i for i in range(1000000)]
random.shuffle(array)

print(array)


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_ar = []
    m_ar = []
    b_ar = []

    for item in array:

        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            b_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception('Случилось непредвиденное!')


    return quick_sort(s_ar) + m_ar + quick_sort(b_ar)


array_new = quick_sort(array)
print(array_new)
