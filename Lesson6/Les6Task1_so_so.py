# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно
# разных значения.

# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
#
# c. результаты анализа (количество занятой памяти в вашей среде разработки)
# вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof
# после каждой переменной, а проявили творчество, фантазию и создали универсальный код для замера памяти.
import sys
from random import randint


# Вариант 1 - решение через сортировку и отсеивание посторяющихся членов через множество
def max_negative_number1(array):
    sort_array = sorted(list(set(array.copy())))
    el = 0
    show_size(sort_array)
    show_size(el)
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
    show_size(max_negative)
    return f'Максимальное отрицательное чиcло {max_negative} расположено на ' \
           f'{array.index(max_negative)} месте в массиве.'

# Вариант 3 - через перебор возможных ответов, посредством движения от -1 в сторону уменьшения
def max_negative_number3(array):
    i = -1
    show_size(i)
    while True:
        for el in array:
            if el == i:
                return f'Максимальное отрицательное чиcло {el} расположено на {array.index(el)} месте в массиве.'
        i -= 1

def show_size(x, level=0):
    print('\t'*level, f'type={x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


print(sys.version, sys.platform)
#3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] win32
list1 = [randint(-10, 10) for _ in range(10)]
print(list1)

print('*' * 100)
max_negative_number1(list1)
print('*' * 100)
max_negative_number2(list1)
print('*' * 100)
max_negative_number3(list1)

# Совершенно не направится решение. Но сделано именно топором,
# т.е. около каждой переменной стоит функция вычисления объема памяти.
# Вывод: Варианты 2 и 3 расходуют памяти меньше всего, так как для их
# функционирования требуется только одна дополнительная переменная типа int.
# В варианте 2 используется копия массия (с корректировкой на уникальные значения),
# что приводит к увеличению требуемой памяти. Но в этом варианте тоже произведена оптимизация решения,
# так как промежуточное множетво по коду меняется на список, который требует меньше памяти.
