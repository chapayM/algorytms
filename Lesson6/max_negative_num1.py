# Вариант 1 - решение через сортировку и отсеивание посторяющихся членов через множество

def max_negative_number1(array):
    sort_array = sorted(list(set(array.copy())))
    i = 0
    while True:
        try:
            if sort_array.index(i) >= 0:
                return f'Максимальное отрицательное чилов {sort_array[sort_array.index(i) - 1]} расположено на ' \
                       f'{array.index(sort_array[sort_array.index(i) - 1])} месте в массиве.', locals()
        except ValueError:
            i += 1

