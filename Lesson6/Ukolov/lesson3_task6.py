# -*- coding: utf-8 -*-
"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint
my_list = [randint(0, 10) for _ in range(10)]
print(my_list)
minimal_pos, maximal_pos = [0, 0]
for i, item in enumerate(my_list):
    if item > my_list[maximal_pos]:
        maximal_pos = i
    if item < my_list[minimal_pos]:
        minimal_pos = i
if minimal_pos > maximal_pos:
    minimal_pos, maximal_pos = maximal_pos, minimal_pos
list_2 = my_list[minimal_pos + 1 : maximal_pos]
print(f"Между минимумом и максимумом: {list_2}")
S = 0
for item in list_2:
    S += item
print(f"Сумма = {S}")


total_memory = 0
import sys
print(sys.version, sys.platform) # 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] win32

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


var_list = [S, i, item, list_2, maximal_pos, minimal_pos, my_list]
show_size(var_list)
print(f"Всего памяти: {total_memory} байт")
# [3, 9, 2, 6, 7, 0, 4, 10, 9, 3]
# Между минимумом и максимумом: [4]
# Сумма = 4
# 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] win32
#  type= <class 'list'>, size=120, object= [4, 9, 4, [4], 7, 5, [3, 9, 2, 6, 7, 0, 4, 10, 9, 3]]
#          type= <class 'int'>, size=28, object= 4
#          type= <class 'int'>, size=28, object= 9
#          type= <class 'int'>, size=28, object= 4
#          type= <class 'list'>, size=72, object= [4]
#                  type= <class 'int'>, size=28, object= 4
#          type= <class 'int'>, size=28, object= 7
#          type= <class 'int'>, size=28, object= 5
#          type= <class 'list'>, size=192, object= [3, 9, 2, 6, 7, 0, 4, 10, 9, 3]
#                  type= <class 'int'>, size=28, object= 3
#                  type= <class 'int'>, size=28, object= 9
#                  type= <class 'int'>, size=28, object= 2
#                  type= <class 'int'>, size=28, object= 6
#                  type= <class 'int'>, size=28, object= 7
#                  type= <class 'int'>, size=24, object= 0
#                  type= <class 'int'>, size=28, object= 4
#                  type= <class 'int'>, size=28, object= 10
#                  type= <class 'int'>, size=28, object= 9
#                  type= <class 'int'>, size=28, object= 3
# Всего памяти: 828 байт
