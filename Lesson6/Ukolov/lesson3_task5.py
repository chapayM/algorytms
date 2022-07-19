# -*- coding: utf-8 -*-
"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
from random import randint
import sys

print(sys.version, sys.platform) # 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] win32
my_list = [randint(-30, 30) for _ in range(10)]
print(my_list)
maximal, pos = 0, -1
for i, item in enumerate(my_list):
    if item < 0 and (maximal == 0 or item > maximal):
        maximal = item
        pos = i
if pos == -1:
    print("Нет отрицательных чисел")
else:
    print(f"Максимальный отрицательный элемент: {maximal}, на {pos} позиции")
total_memory = 0


def show_size(x, level=0):
    global total_memory
    print('\t' * level, f'type= {x.__class__}, size={sys.getsizeof(x)}, object= {x}')
    total_memory = total_memory + sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


var_list = [i, item, maximal, my_list, pos]
show_size(var_list)
print(f"Всего памяти: {total_memory} байт")
#[-8, -11, 11, 13, 2, -26, -15, 24, -8, 13]
#Максимальный отрицательный элемент: -8, на 0 позиции
#  type= <class 'list'>, size=104, object= [9, 13, -8, [-8, -11, 11, 13, 2, -26, -15, 24, -8, 13], 0]
#          type= <class 'int'>, size=28, object= 9
#          type= <class 'int'>, size=28, object= 13
#          type= <class 'int'>, size=28, object= -8
#          type= <class 'list'>, size=192, object= [-8, -11, 11, 13, 2, -26, -15, 24, -8, 13]
#                  type= <class 'int'>, size=28, object= -8
#                  type= <class 'int'>, size=28, object= -11
#                  type= <class 'int'>, size=28, object= 11
#                  type= <class 'int'>, size=28, object= 13
#                  type= <class 'int'>, size=28, object= 2
#                  type= <class 'int'>, size=28, object= -26
#                  type= <class 'int'>, size=28, object= -15
#                  type= <class 'int'>, size=28, object= 24
#                  type= <class 'int'>, size=28, object= -8
#                  type= <class 'int'>, size=28, object= 13
#          type= <class 'int'>, size=24, object= 0
# Всего памяти: 684 байт
