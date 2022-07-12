# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

import cProfile
import timeit

def row_numbers(num_el, el, total):
    if num_el == 0:
        return total
    else:
        total = total + el
        el = el / -2
        num_el = num_el - 1
        return row_numbers(num_el, el, total)


"""
cProfile.run("row_numbers(5,1,0)")
9 function calls (4 primitive calls) in 0.000 seconds
6/1       0.000     0.000    0.000    0.000 les_4_task_1.py:6(row_numbers) 

cProfile.run("row_numbers(50,1,0)")
54 function calls (4 primitive calls) in 0.000 seconds
51/1      0.000     0.000    0.000    0.000 les_4_task_1.py:6(row_numbers) 

cProfile.run("row_numbers(500,1,0)")
504 function calls (4 primitive calls) in 0.002 seconds
501 / 1   0.001     0.000    0.001    0.001 les_4_task_1.py:6(row_numbers) 



"les_4_task_1.row_numbers(5, 1, 0)"
1000 loops, best of 5: 1.15 usec per loop

"les_4_task_1.row_numbers(50, 1, 0)"
#1000 loops, best of 5: 10.2 usec per loop

les_4_task_1.row_numbers(500,1, 0)"
1000 loops, best of 5: 113 usec per loop
"""

""" 
Используем рекурсию. Время выполнения алгоритма прямо пропорционально входным данным.
Работает медленно,особенно при больших данных. В случае,если вызываемых функций будет очень много,
может произойти переполнение стеков.
Однако при рекурсии, при каждом входе в нее, все начинается с "чистого" листа, то есть не надо тратиться на память.
В рекурсии - более короткий, наглядный код."""