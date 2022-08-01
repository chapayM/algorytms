#<Быстрая сортировка Хоара доп переменной. Сложность O(n^2) максимальная, до O(n log n).
# Неустойчивая. Тип - Обменная. Требует доп память - не требуется

import random

array = [i for i in range(1000)]
random.shuffle(array)

print(array)


def quick_sort_no_memory(array, fst=0, lst=len(array) -1):

    if fst >= lst:
        return

    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <= j:

        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

    quick_sort_no_memory(array, fst, j)
    quick_sort_no_memory(array, i, lst)

quick_sort_no_memory(array)
print(array)
