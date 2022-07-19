# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно
# разных значения.
import sys
from random import randint


# Вариант 1 - решение через сортировку и отсеивание посторяющихся членов через множество
def max_negative_number1(array):
    sort_array = sorted(list(set(array.copy())))
    el = 0
    while True:
        try:
            if sort_array.index(el)>=0:
                return f'Максимальное отрицательное чилов {sort_array[sort_array.index(el)-1]} расположено на ' \
                       f'{array.index(sort_array[sort_array.index(el)-1])} месте в массиве.'
        except ValueError:
            el += 1

# Вариант 2 - решение без применения сортировки c последовательным перебором всех членов списка
def max_negative_number2(array):
    max_negative = 0
    for el in array:
        if el < 0 and max_negative == 0:
            max_negative = el
        elif el < 0 and max_negative != 0:
            if max_negative < el:
                max_negative = el
    return f'Максимальное отрицательное чиcло {max_negative} расположено на ' \
           f'{array.index(max_negative)} месте в массиве.'

# Вариант 3 - через перебор возможных ответов, посредством движения от -1 в сторону уменьшения
def max_negative_number3(array):
    i = -1
    while True:
        for el in array:
            if el == i:
                return f'Максимальное отрицательное чиcло {el} расположено на {array.index(el)} месте в массиве.'
        i -= 1



list1 = [randint(-10, 10) for _ in range(1000)]
print(list1)
print(max_negative_number1(list1))
print(max_negative_number2(list1))
print(max_negative_number3(list1))
