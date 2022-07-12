# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.'''

import cProfile
import timeit

def row_n(n):
    ls = []
    num = 1
    for _ in range(n):
        ls.append(num)
        num *= -0.5
    total = sum(ls)
    return total

"""
cProfile.run("row_n(5)")
 10 function calls in 0.000 seconds
 1    0.000    0.000    0.000   0.000      les_4_task_3.py: 7(row_n)
 5    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run("row_n(50)")
 55 function calls in 0.000 seconds
 1    0.000    0.000    0.000   0.000      les_4_task_3.py: 7(row_n)
 50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

cProfile.run("row_n(500)")
 505 function calls in 0.001 seconds
 1    0.000    0.000    0.000   0.000      les_4_task_3.py: 7(row_n)
 500    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


"les_4_task_3.row_n(5)"
1000 loops, best of 5: 1.47 usec per loop

"les_4_task_3.row_n(50)"
1000 loops, best of 5: 8.79 usec per loop

"les_4_task_3.row_n(500)"
1000 loops, best of 5: 62.5 usec per loop
"""


"""
Используем цикл+список.
Время выполнения алгоритма не пропорционально входным данным.
Данное сочетание быстрее рекурсии и цикла, особенно при больших входных данных.
Считаю что данный алгоритм лучший вариант, тк занимает наименьшее компьютерное время для вычисления, особенно 
при больших входных данных. Надеюсь,что и памяти занимает немного при работе. 
"""