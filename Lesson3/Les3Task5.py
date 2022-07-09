# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно
# разных значения.

from random import randint


# def max_negative_number(array):
#     sort_array = sorted(list(set(array.copy())))
#     el = 0
#     while True:
#         try:
#             if sort_array.index(el)>=0:
#                 return f'Максимальное отрицательное чилов {sort_array[sort_array.index(el)-1]} расположено на ' \
#                        f'{array.index(sort_array[sort_array.index(el)-1])} месте в массиве.'
#         except ValueError:
#             el+=1

def max_negative_number(array):
    max_negative = 0
    for el in array:
        if el < 0 and max_negative == 0:
            max_negative = el
        elif el < 0 and max_negative != 0:
            if max_negative < el:
                max_negative = el
    return f'Максимальное отрицательное чиcло {max_negative} расположено на ' \
           f'{array.index(max_negative)} месте в массиве.'


list1 = [randint(-100, 100) for _ in range(10)]
print(list1)
print(max_negative_number(list1))
