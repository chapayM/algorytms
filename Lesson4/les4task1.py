# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
# первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких
# N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.
import cProfile
from random import randint

# Вариант 1 (без функции sorted)
# def sum_between_max_min(x, y):
#     array= [randint(0, x) for _ in range(y)]
#     max_el = array[0]
#     min_el = array[0]
#     i = 0
#     while i < len(array) - 1:
#         if max_el < array[i + 1]:
#             max_el = array[i + 1]
#         if min_el > array[i + 1]:
#             min_el = array[i + 1]
#         i += 1
#     index_min, \
#     index_max = array.index(min_el), array.index(max_el)
#     sum_res = 0
#     if index_min < index_max:
#         for el in array[index_min + 1:index_max]:
#             sum_res += el
#     else:
#         for el in array[index_max + 1:index_min]:
#             sum_res += el
#     return sum_res
# 1000 loops, best of 5: 12.2 usec per loop для массива в 10 значений, при числах от 0 до 20
#  75 function calls in 0.000 seconds
# 1000 loops, best of 5: 113 usec per loop для массива в 100 значений, при числах от 0 до 20
# 675 function calls in 0.000 seconds
# 1000 loops, best of 5: 8.45 msec per loop для массива в 10000 значений, при числах от 0 до 20
# 65282 function calls in 0.029 seconds
# 1000 loops, best of 5: 12.8 usec per loop для масиива в 10 значений, при числах от 0 до 2000
# 1000 loops, best of 5: 122 usec per loop, для массива в 100 значений, при числах от 0 до 2000
# 1000 loops, best of 5: 9.26 msec per loop, для массива в 10000 значений, при числах от 0 до 2000
# 60256 function calls in 0.029 seconds


# Вариант 2. С функцией sorted
# def sum_between_max_min(x, y):
#     array= [randint(0, x) for _ in range(y)]
#     sort_array = sorted(array.copy())
#     index_min, index_max = array.index(sort_array[0]), array.index(sort_array[-1])
#     sum_res = 0
#     if index_min < index_max:
#         for el in array[index_min + 1:index_max]:
#             sum_res += el
#     else:
#         for el in array[index_max + 1:index_min]:
#             sum_res += el
#     return sum_res
# 1000 loops, best of 5: 11 usec per loop для массива в 10 значений, при числах от 0 до 20
# 63 function calls in 0.000 seconds
# 1000 loops, best of 5: 102 usec per loop для массива в 100 значений, при числах от 0 до 20
# 561 function calls in 0.000 seconds
# 1000 loops, best of 5: 7.51 msec per loop для массива в 10000 значений, при числах от 0 до 20
# 55448 function calls in 0.024 seconds
# 1000 loops, best of 5: 11.4 usec per loop для масиива в 10 значений, при числах от 0 до 2000
# 1000 loops, best of 5: 112 usec per loop, для массива в 100 значений, при числах от 0 до 2000
# 1000 loops, best of 5: 8.51 msec per loop, для массива в 10000 значений, при числах от 0 до 2000
# 50237 function calls in 0.026 seconds



# Вариант 3 использованием срезов, мах, min и sum
def sum_between_max_min(x, y):
    array= [randint(0, x) for _ in range(y)]
    index_min_max = sorted([array.index(min(array)), array.index(max(array))])
    return sum(array[index_min_max[0]:index_min_max[1]])
# 1000 loops, best of 5: 11.1 usec per loop для массива в 10 значений, при числах от 0 до 20
# 62 function calls in 0.000 seconds
# 1000 loops, best of 5: 97 usec per loop для массива в 100 значений, при числах от 0 до 20
# 569 function calls in 0.000 seconds
# 1000 loops, best of 5: 6.83 msec per loop для массива в 10000 значений, при числах от 0 до 20
# 55156 function calls in 0.025 seconds
# 1000 loops, best of 5: 11.6 usec per loop для масиива в 10 значений, при числах от 0 до 2000
# 1000 loops, best of 5: 106 usec per loop, для массива в 100 значений, при числах от 0 до 2000
# 1000 loops, best of 5: 7.44 msec per loop, для массива в 10000 значений, при числах от 0 до 2000
# 50244 function calls in 0.025 seconds

cProfile.run('sum_between_max_min(2000,10000)')

# Общий вывод по оптимальности:
# 3 вариант решения задачи через использование срезов, функций max,
# min, sum, sorted является наиболее оптимальным по требованиям к
# ресурсам, хотя и не кардинально отличается от других варинатов,
# включая вариант 1, где функции поиска максимального и минимального
# значения и суммирования написаны самостоятельно. Стандартные функции
# max, min, sum скорее всего максимально оптимизированы разработчиками
# язка.Так же в положительной стороне 3 варианта относится
# минимальность кода и простота его чтения.
# Выбираем вариант 3!
