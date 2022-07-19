# Вариант 2 - решение без применения сортировки c последовательным перебором всех членов списка
def max_negative_number2(array, arr_var):
    max_negative = 0
    for el in array:
        if el < 0 and max_negative == 0:
            max_negative = el
        elif el < 0 and max_negative != 0:
            if max_negative < el:
                max_negative = el
    return f'Максимальное отрицательное чиcло {max_negative} расположено на ' \
           f'{array.index(max_negative)} месте в массиве.'