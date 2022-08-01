# Сортировака вставками. Сложность O(n^2) максимальная, до O(n).
# Устойчивая. Тип - Вставками. Требует доп память - не требуется

import random

array = [i for i in range(1000)]
random.shuffle(array)

print(array)


def insertion_sort(array):
    count = 0
    for i in range(1, len(array)):
        spam = array[i]
        j = i

        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
            count += 1
        array[j] = spam
    print(count)


insertion_sort(array)
print(array)
