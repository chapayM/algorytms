# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».

import cProfile

# Так как нам надо вернуть i то тут есть ограничение, которое пока перекрыто чисто условно, и безусловно, не 100%
def getNumSieve(c):
    sieve_size = c*100

    sieve    = [x for x in range(sieve_size)]
    sieve[1] = 0

    for i in range(2, sieve_size):
        if sieve[i] != 0:
            j = i * 2

            while j < sieve_size:
                sieve[j] = 0
                j += i

    result = [x for x in sieve if x != 0]
    if (len(result) >= c) and (len(result)>0):
        return result[c - 1]
    else:
        return False

# print(getNumSieve(1))

# Результат профилирования
# cProfile.run('getNumSieve(129000)')
#          8 function calls in 6.253 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.095    0.095    6.253    6.253 <string>:1(<module>)
#         1    0.498    0.498    0.498    0.498 task_02.py:12(<listcomp>)
#         1    0.328    0.328    0.328    0.328 task_02.py:23(<listcomp>)
#         1    5.332    5.332    6.158    6.158 task_02.py:9(getNumSieve)
#         1    0.000    0.000    6.253    6.253 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вторая реализация
def getPrimeNum(n):

    # Определяет для любого число, простое оно или нет методом общих делителей.
    def numSimple(num):
        i = 4
        j = 0

        while i*i <= num and j != 1:
            if num % i == 0:
                j = 1

            i += 1

        if j != 1:
            return num
        else:
            return False


    if n == 1:
        return 2

    if n == 2:
        return 3

    curent_num_simple = 3
    curent_num = 5

    while curent_num_simple <= n:
        if curent_num % 2 == 0:
            pass
        elif curent_num % 3 == 0:
            pass
        else:
            num = numSimple(curent_num)
            if num != False:
                curent_num_simple += 1

        curent_num += 1

    return num

#print(getPrimeNum(129000))

cProfile.run('getPrimeNum(129000)')

# 570788 function calls in 22.078 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   22.078   22.078 <string>:1(<module>)
#         1    0.317    0.317   22.078   22.078 task_02.py:48(getPrimeNum)
#    570784   21.762    0.000   21.762    0.000 task_02.py:51(numSimple)
#         1    0.000    0.000   22.078   22.078 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#          570788 function calls in 24.805 seconds


#print(getNumSieve(129000))
#print(getPrimeNum(129000))

# ===============================================================================================
# На метод прямого перебора уходит много времени что о чём и говорилось, разница почти в три раза
# и решето работает быстрее, несмотря даже на увелечение самого решета не оптимальным способом, на бум
# Возможно если применить "достройку" решета, можно будет добиться ещё лучших результатов по времени, и избежать
# неоднозначности, при выходе за пределы решета.
