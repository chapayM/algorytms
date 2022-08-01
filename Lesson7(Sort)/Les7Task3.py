# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался
# на уроках (сортировка слиянием также недопустима).

import random

array = [i for i in range(1, 100)]
random.shuffle(array)
print(array)

def median(array):
    med_count = len(array) // 2
    for i in range(len(array)):
        max_count = min_count = 0
        for j in range(len(array)):
            if array[i]>array[j]:
                min_count += 1
            elif array[i]<array[j]:
                max_count += 1
            if max_count == min_count == med_count:
                return array[i]


print(median(array))

