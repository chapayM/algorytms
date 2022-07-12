"""
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего
задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
"""

import random
import cProfile

# Первый вариант из ТЗ, слегка модернизированный чтобы удобнее было
# вызывать с массивом извне и нет
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
def changMinMax(c, d=None):
    if (d == None):
        d = [random.randint(1, 110) for _ in range(c)]

    minValue = maxValue = d[0]
    minIndex = maxIndex = 0

    for index, value in enumerate(d):
        if value >= maxValue:
            maxValue = value
            maxIndex = index

        if value <= minValue:
            minValue = value
            minIndex = index

    d[minIndex] = maxValue
    d[maxIndex] = minValue

    return d

# Результаты замеров для массива разной длинны
# 1000 loops, best of 5: 9.32 usec per loop    c=10**1
# 1000 loops, best of 5: 86.5 usec per loop    c=10**2
# 1000 loops, best of 5: 898 usec per loop     c=10**3
# 1000 loops, best of 5: 9.13 msec per loop    c=10**4
# 1000 loops, best of 5: 97.7 msec per loop    c=10**5
# 1000 loops, best of 5: 1.05 sec per loop     c=10**6
# 10 loops, best of 5: 9.82 sec per loop       c=10**7
# 10 loops, best of 5: 98.4 sec per loop       c=10**8

# Выдача cProfile не очень информативная, но интересно что при создании массива метод
# getrandbits вызывается на +/- 15% больше

#   5163133 function calls in 1.636 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001    1.636    1.636 <string>:1(<module>)
#  1000000    0.546    0.000    1.144    0.000 random.py:174(randrange)
#  1000000    0.222    0.000    1.366    0.000 random.py:218(randint)
#  1000000    0.424    0.000    0.598    0.000 random.py:224(_randbelow)
#        1    0.060    0.060    1.634    1.634 task_01.py:17(changMinMax)
#        1    0.209    0.209    1.574    1.574 task_01.py:19(<listcomp>)
#        1    0.000    0.000    1.636    1.636 {built-in method builtins.exec}
#  1000000    0.057    0.000    0.057    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  1163128    0.118    0.000    0.118    0.000 {method 'getrandbits' of '_random.Random' objects}

# 2. Пишем второй вариант
def changMinMax2(c, d=None):
    if (d == None):
        d = [random.randint(1, 110) for _ in range(c)]

    # Получили сами значения уже
    n = sorted(d)
    minvalue = n[0]
    maxvalue = n[-1]

    # осталось только найти их индексы в массиве
    minindex = maxindex = 0

    for index, value in enumerate(d):
        if value == maxvalue and maxindex == 0:
            maxindex = index

        if value == minvalue and minindex == 0:
            minindex = index

        if minindex > 0 and maxindex > 0:
            break

    d[minindex],d[maxindex] = maxvalue, minvalue
    return d


#              changMinMax                                        changMinMax2
# 1000 loops, best of 5: 9.32 usec per loop    c=10**1      1000 loops, best of 5: 9.2 usec per loop
# 1000 loops, best of 5: 86.5 usec per loop    c=10**2      1000 loops, best of 5: 85.7 usec per loop
# 1000 loops, best of 5: 898 usec per loop     c=10**3      1000 loops, best of 5: 863 usec per loop
# 1000 loops, best of 5: 9.13 msec per loop    c=10**4      1000 loops, best of 5: 8.8 msec per loop
# 1000 loops, best of 5: 97.7 msec per loop    c=10**5      1000 loops, best of 5: 95.8 msec per loop
# 1000 loops, best of 5: 1.05 sec per loop     c=10**6
# 10 loops, best of 5: 9.82 sec per loop       c=10**7
# 10 loops, best of 5: 98.4 sec per loop       c=10**8

# Результаты чуть получше, что и следовало ожидать, но не намного, тем более, что скорость будет зависеть
# от того как далеко в массиве стоит последний элемент, потому дальше не продолжаем переходим к третьему варианту.

def changMinMax3(c, d=None):
    if (d == None):
        d = [random.randint(1, 110) for _ in range(c)]

    # Получили сами значения уже
    tmpdict = dict(zip([x for x in range(c)], d))
    tmpdict = sorted(tmpdict.items(), key=lambda x: x[1])

    #print(tmpdict)
    #print(d)
    minvalue = tmpdict[0][1]
    maxvalue = tmpdict[-1][1]

    minindex = tmpdict[0][0]
    maxindex = tmpdict[-1][0]

    d[minindex],d[maxindex] = maxvalue, minvalue
    return d

#c = 10**1
#d = [random.randint(1, 110) for _ in range(c)]
#cProfile.run('changMinMax(c)')
#r = changMinMax3(c)
#print(r)

#              changMinMax                                        changMinMax2                                      changMinMax3
# 1000 loops, best of 5: 9.32 usec per loop    c=10**1      1000 loops, best of 5: 9.2 usec per loop        1000 loops, best of 5: 12 usec per loop
# 1000 loops, best of 5: 86.5 usec per loop    c=10**2      1000 loops, best of 5: 85.7 usec per loop       1000 loops, best of 5: 96.6 usec per loop
# 1000 loops, best of 5: 898 usec per loop     c=10**3      1000 loops, best of 5: 863 usec per loop        1000 loops, best of 5: 990 usec per loop
# 1000 loops, best of 5: 9.13 msec per loop    c=10**4      1000 loops, best of 5: 8.8 msec per loop        1000 loops, best of 5: 10.7 msec per loop
# 1000 loops, best of 5: 97.7 msec per loop    c=10**5      1000 loops, best of 5: 95.8 msec per loop       1000 loops, best of 5: 123 msec per loop
# 1000 loops, best of 5: 1.05 sec per loop     c=10**6      10 loops, best of 5: 954 msec per loop          10 loops, best of 5: 1.28 sec per loop
# 10 loops, best of 5: 9.82 sec per loop       c=10**7
# 10 loops, best of 5: 98.4 sec per loop       c=10**8

# Вывод:
# пример возможно не очень удачный получился, но:
# 1: Реализация changMinMax2 стала чуть лучше, так как позволяет при стечении обстоятельств быть чуть быстрее изначального враианта.
#    Но увелчено использует память так как создается сортируемый список
# 2: changMinMax3 Несмотря на то, что содержит мало кода работает медленне, что и понятно, так как несколько раз трасформирует список с данными.
#    и требует больше памяти, хотя разница ну прям не безумно огромная по скорости.
#
# 3: В результате, самый первый алгоритм остается фаворитом, так как меньше требователен к памяти, при не значительном проигрыше в скорости.

