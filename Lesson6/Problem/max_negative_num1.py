# Вариант 1 - решение через сортировку и отсеивание посторяющихся членов через множество
from def_show_size import show_size


def max_negative_number1(array):
    sort_array = sorted(list(set(array.copy())))
    print(locals())
    i = 0
    print(locals())
    while True:
        try:
            if sort_array.index(i) >= 0:
                return f'Максимальное отрицательное чилов {sort_array[sort_array.index(i) - 1]} расположено на ' \
                       f'{array.index(sort_array[sort_array.index(i) - 1])} месте в массиве.'
        except ValueError:
            i += 1
            print(locals())


print(globals())
print(globals().items())
max_negative_number1([-10, 2, -3, 5, 1, -1])
print(locals())