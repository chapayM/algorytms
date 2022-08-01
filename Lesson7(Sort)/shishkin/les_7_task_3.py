"""
Задание 3
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. 
Но если это слишком сложно, используйте метод сортировки, который не рассматривался
на уроках (сортировка слиянием также недопустима).
"""
from les_7_task_1 import get_array


def mediana_search(array, min):
    idx_mediana = len(array) // 2
    idxs = set()
    for _ in range(idx_mediana + 1):
        _idx = 0
        _min = min
        for idx, el in enumerate(array):
            if el > _min and idx not in idxs:
                _min = el
                _idx = idx
        idxs.add(_idx)
    else:
        print(f'Медианой является элемент "{_min}"')


if __name__ == "__main__":
    m = 5
    min = -50
    size = 2 * m + 1
    array = get_array(size, min, 50)
    print(array)
    mediana_search(array, min)
    print(array)
