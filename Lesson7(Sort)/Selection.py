# Сортировака выбором. Сложность O(n^2).
# Устойчивая/неустойчивая. Тип - Выбором. Требует доп память - не требуется


import random

array = [i for i in range(1000)]
random.shuffle(array)

print(array)


def selection_sort(array):
    count = 0
    for i in range(len(array)):
        idx_min = i

        for j in range(i + 1, len(array)):
            count += 1
            if array[j] < array[idx_min]:
                idx_min = j

        array[idx_min], array[i] = array[i], array[idx_min]
    print(count)
#Возвращать ничего не нужно, так как список это ссылочная структура и сортируя его в самой функции,
# мы изменяем его в глобальной переменной

selection_sort(array)
print(array)
