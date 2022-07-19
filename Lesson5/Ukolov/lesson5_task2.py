# -*- coding: utf-8 -*-
"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections
first, operand, second = list(input("1 число: ")), input("операция (+ или *): "), list(input("2 число: "))
hex_to_int = {'0':0 , '1':1, '2':2,'3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
int_to_hex = {x:y for y, x in hex_to_int.items()}
res = collections.deque([])
in_memory = 0
for_res = 0
if operand == '+':
    if len(second) > len(first):
        first, second = second, first
    for i in range(-1, -1-1*len(second), -1):
        for_res = hex_to_int[second[i]] + hex_to_int[first[i]] + in_memory
        in_memory = 0
        if for_res >=16:
            in_memory = for_res //16
            for_res %= 16
        res.appendleft(int_to_hex[for_res])
    for i in range(-1-1*len(second), -1-1*len(first), -1):
        for_res = hex_to_int[first[i]] + in_memory
        in_memory = 0
        if for_res >=16:
            in_memory = for_res //16
            for_res %= 16
        res.appendleft(int_to_hex[for_res])
    res = list(res)
elif operand == '*':
    for_sum = collections.deque([])
    sum_list = []
    if len(second) > len(first):
        first, second = second, first
    for i in range(-1, -1-1*len(second), -1):
        for j in range(-1, -1-1*len(first), -1):
            for_res = hex_to_int[second[i]] * hex_to_int[first[j]] + in_memory
            in_memory = 0
            if for_res >=16:
                in_memory = for_res //16
                for_res %= 16
            for_sum.appendleft(for_res)
        sum_list.append(list(for_sum) + [0,]*(-1 * i - 1))
        for_sum.clear()
    max_len = 0
    for i in range(0, len(sum_list)):
        if len(sum_list[i]) > max_len:
            max_len = len(sum_list[i])
    for i in range(0, len(sum_list)):
        delta_len = max_len - len(sum_list[i])
        sum_list[i] = [0] * delta_len + sum_list[i]
    for i in range(-1, -1-1*max_len, -1):
        for_res = in_memory
        for j in range(0, len(sum_list)):
            for_res += sum_list[j][i]
        in_memory = 0
        if for_res >=16:
            in_memory = for_res //16
            for_res %= 16
        res.appendleft(int_to_hex[for_res])
    res = list(res)
else:
    print("Ошибка - недопустимая операция")
print(res)
