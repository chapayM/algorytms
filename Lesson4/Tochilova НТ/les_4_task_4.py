### 2. Написать два алгоритма нахождения i-го по счёту простого числа.
### Без использования «Решета Эратосфена»;

import cProfile
import timeit
import math

def sieve_without_eratosthenes(i):
    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


"""
"les_4_task_4.sieve_without_eratosthenes(5)"
1000 loops, best of 5: 4.12 usec per loop


"les_4_task_4.sieve_without_eratosthenes(50)"
1000 loops, best of 5: 162 usec per loop


"les_4_task_4.sieve_without_eratosthenes(500)"
1000 loops, best of 5: 12.2 msec per loop



cProfile.run("sieve_without_eratosthenes(5)")
27 function calls in 0.000 seconds
10    0.000    0.000    0.000    0.000 {built-in method builtins.len}
4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
9    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run("sieve_without_eratosthenes(50)")
508 function calls in 0.001 seconds
1      0.000    0.000    0.001    0.001 <string>:1(<module>)
1      0.001    0.001    0.001    0.001 les_4_task_4.py:8(sieve_without_eratosthenes)
1      0.000    0.000    0.001    0.001 {built-in method builtins.exec}
228    0.000    0.000    0.000    0.000 {built-in method builtins.len}
49     0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
227    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
1      0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run("sieve_without_eratosthenes(500)")
7642 function calls in 0.023 seconds
1       0.000    0.000    0.023    0.023 <string>:1(<module>)
1       0.021    0.021    0.023    0.023 les_4_task_4.py:8(sieve_without_eratosthenes)
1       0.000    0.000    0.023    0.023 {built-in method builtins.exec}
3570    0.000    0.000    0.000    0.000 {built-in method builtins.len}
499     0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
3569    0.002    0.000    0.002    0.000 {method 'copy' of 'list' objects}
1       0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
Очень странно, но данный алгоритм, без использования "Решета Эратосфена", занял меньше компьютерного времени.
При нахождении пятого постого числа функция вызывалась 27 раз
При нахождении 50-го простого числа - 228 раз, при 500 - 7642 раза"""