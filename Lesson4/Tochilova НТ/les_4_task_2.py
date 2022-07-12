# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.'''

import cProfile
import timeit

def row_n(n):
    i = 0
    range_number = 1
    sum = 0
    while i < n:
        sum += range_number
        range_number /= -2
        i += 1
    return sum

"""
cProfile.run("row_n(5)")
4 function calls in 0.000 seconds
1    0.000    0.000    0.000   0.000  les_4_task_2.py: 7(row_n)   

cProfile.run("row_n(50)")
4 function calls in 0.000 seconds
1    0.000    0.000    0.000   0.000  les_4_task_2.py: 7(row_n)   

cProfile.run("row_n(500)")
4 function calls in 0.000 seconds
1    0.000    0.000    0.000   0.000  les_4_task_2.py: 7(row_n)   



"les_4_task_2.row_n(5)"
1000 loops, best of 5: 2.82 usec per loop

"les_4_task_2.row_n(50)"
1000 loops, best of 5: 10.4 usec per loop

"les_4_task_2.row_n(500)"
1000 loops, best of 5: 96.1 usec per loop
"""

"""
Используем цикл.  Время выполнения алгоритма прямо пропорционально входным данным.
При малом количестве данных - медленнее рекурсии, однако при большом количестве данных (500) - быстрее рекурсии."""