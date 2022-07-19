# -*- coding: utf-8 -*-
"""
Определить, какое число в массиве встречается чаще всего.
"""
from random import randint
my_list = [randint(0, 9) for _ in range(20)]
print(my_list)
my_dict = {}
for item in my_list:
    if my_dict.get(item) == None:
        my_dict[item] = 0
    my_dict[item] += 1
max_value, max_key = 0, None
for key, value in my_dict.items():
    if value > max_value:
        max_value = value
        max_key = key
print(f"Чаще всего встречается {max_key} - {max_value} раз")


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


var_list = [item, key, max_key, max_value, my_dict, my_list, value]
show_size(var_list)
print(f"Всего памяти: {total_memory} байт")


# [3, 3, 1, 5, 6, 2, 4, 5, 4, 8, 4, 9, 9, 4, 5, 4, 4, 4, 6, 9]
# Чаще всего встречается 4 - 7 раз
#  type= <class 'list'>, size=120, object= [9, 9, 4, 7, {3: 2, 1: 1, 5: 3, 6: 2, 2: 1, 4: 7, 8: 1, 9: 3}, [3, 3, 1, 5, 6, 2, 4, 5, 4, 8, 4, 9, 9, 4, 5, 4, 4, 4, 6, 9], 3]
#          type= <class 'int'>, size=28, object= 9
#          type= <class 'int'>, size=28, object= 9
#          type= <class 'int'>, size=28, object= 4
#          type= <class 'int'>, size=28, object= 7
#          type= <class 'dict'>, size=368, object= {3: 2, 1: 1, 5: 3, 6: 2, 2: 1, 4: 7, 8: 1, 9: 3}
#                  type= <class 'tuple'>, size=64, object= (3, 2)
#                          type= <class 'int'>, size=28, object= 3
#                          type= <class 'int'>, size=28, object= 2
#                  type= <class 'tuple'>, size=64, object= (1, 1)
#                          type= <class 'int'>, size=28, object= 1
#                          type= <class 'int'>, size=28, object= 1
#                  type= <class 'tuple'>, size=64, object= (5, 3)
#                          type= <class 'int'>, size=28, object= 5
#                          type= <class 'int'>, size=28, object= 3
#                  type= <class 'tuple'>, size=64, object= (6, 2)
#                          type= <class 'int'>, size=28, object= 6
#                          type= <class 'int'>, size=28, object= 2
#                  type= <class 'tuple'>, size=64, object= (2, 1)
#                          type= <class 'int'>, size=28, object= 2
#                          type= <class 'int'>, size=28, object= 1
#                  type= <class 'tuple'>, size=64, object= (4, 7)
#                          type= <class 'int'>, size=28, object= 4
#                          type= <class 'int'>, size=28, object= 7
#                  type= <class 'tuple'>, size=64, object= (8, 1)
#                          type= <class 'int'>, size=28, object= 8
#                          type= <class 'int'>, size=28, object= 1
#                  type= <class 'tuple'>, size=64, object= (9, 3)
#                          type= <class 'int'>, size=28, object= 9
#                          type= <class 'int'>, size=28, object= 3
#          type= <class 'list'>, size=264, object= [3, 3, 1, 5, 6, 2, 4, 5, 4, 8, 4, 9, 9, 4, 5, 4, 4, 4, 6, 9]
#                  type= <class 'int'>, size=28, object= 3
#                  type= <class 'int'>, size=28, object= 3
#                  type= <class 'int'>, size=28, object= 1
#                  type= <class 'int'>, size=28, object= 5
#                  type= <class 'int'>, size=28, object= 6
#                  type= <class 'int'>, size=28, object= 2
#                  type= <class 'int'>, size=28, object= 4
#                  type= <class 'int'>, size=28, object= 5
#                  type= <class 'int'>, size=28, object= 4
#                  type= <class 'int'>, size=28, object= 8
#                  type= <class 'int'>, size=28, object= 4
#                  type= <class 'int'>, size=28, object= 9
#                  type= <class 'int'>, size=28, object= 9
#                  type= <class 'int'>, size=28, object= 4
#                  type= <class 'int'>, size=28, object= 5
#                  type= <class 'int'>, size=28, object= 4
#                  type= <class 'int'>, size=28, object= 4
#                  type= <class 'int'>, size=28, object= 4
#                  type= <class 'int'>, size=28, object= 6
#                  type= <class 'int'>, size=28, object= 9
#          type= <class 'int'>, size=28, object= 3
# Всего памяти: 2412 байт
