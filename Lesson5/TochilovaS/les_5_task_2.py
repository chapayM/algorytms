"""Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
 массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""

from collections import deque
import timeit

num_1 = deque(['A', '2'])
num_2 = deque(['C', '4', 'F'])
dict_num_hexa = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
k = 0 # k - степень в которую мы возводим число
num_1.reverse()
num_2.reverse()

# Переводим шестнадцатеричное число в десятичное
new_num_1 = []
new_num_2 = []
for i in num_1:
    a = dict_num_hexa[i]
    a = a * 16 ** k
    new_num_1.append(a)
    k += 1
k = 0
for i in num_2:
    a = dict_num_hexa[i]
    a = a * 16 ** k
    new_num_2.append(a)
    k += 1

# Находим сумму и произведение чисел в десятичной системе счисления
sum_ = sum(new_num_2+new_num_1)
multiplic = (sum(new_num_1)) * (sum(new_num_2))

# Переводим десятичные числа в шестнадцатеричные
ls = []
if sum_ < 16:
    a = dict_num_hexa(sum_)
else:
    while sum_ > 16:
        ostatok = sum_ % 16
        ls.append(ostatok)
        sum_ = sum_ // 16
ls.append(sum_)
ls.reverse()
ls_n = []
for i in ls:
    a = dict_num_hexa[i]
    ls_n.append(a)

ls_multip = []
if multiplic < 16:
    a = dict_num_hexa(multiplic)
else:
    while multiplic > 16:
        ostatok = multiplic % 16
        ls_multip.append(ostatok)
        multiplic = multiplic // 16
ls_multip.append(multiplic)
ls_multip.reverse()
ls_multip_n = []
for i in ls_multip:
    a = dict_num_hexa[i]
    ls_multip_n.append(a)

print(f"Сумма чисел равна {ls_n}")
print(f"Произведение чисел равна {ls_multip_n}")





