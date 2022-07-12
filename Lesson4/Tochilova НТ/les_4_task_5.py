# Написать два алгоритма нахождения i-го по счёту простого числа.
# Используя алгоритм «Решето Эратосфена»

import cProfile
import timeit
import math

def sieve_eratosthenes(i):
    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]


def prime_counting_function(i):
    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number



"""
"les_4_task_5.sieve_eratosthenes(5)"
#1000 loops, best of 5: 15.6 usec per loop

"les_4_task_5.sieve_eratosthenes(50)"
1000 loops, best of 5: 2.38 msec per loop

"les_4_task_5.sieve_eratosthenes(500)"
1000 loops, best of 5: 417 msec per loop


cProfile.run("sieve_eratosthenes(5)")
36 function calls in 0.000 seconds
6     0.000    0.000    0.000    0.000 {built-in method builtins.len}
12    0.000    0.000    0.000    0.000 {built-in method math.log}

cProfile.run("sieve_eratosthenes(50)")
631 function calls in 0.006 seconds
1      0.000    0.000    0.006    0.006 <string>:1(<module>)
1      0.005    0.005    0.006    0.006 les_4_task_5.py:8(sieve_eratosthenes)
1      0.000    0.000    0.006    0.006 {built-in method builtins.exec}
61     0.000    0.000    0.000    0.000 {built-in method builtins.len}
282    0.000    0.000    0.000    0.000 {built-in method math.log}
61     0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
221    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}

cProfile.run("sieve_eratosthenes(500)")
8913 function calls in 0.707 seconds
1       0.000    0.000    0.707    0.707 <string>:1(<module>)
1       0.003    0.003    0.004    0.004 les_4_task_5.py:22(prime_counting_function)
1       0.659    0.659    0.707    0.707 les_4_task_5.py:8(sieve_eratosthenes)
1       0.000    0.000    0.707    0.707 {built-in method builtins.exec}
573     0.000    0.000    0.000    0.000 {built-in method builtins.len}
4767    0.001    0.000    0.001    0.001 {built-in method math.log}
573     0.002    0.000    0.002    0.000 {method 'index' of 'list' objects}
3594    0.041    0.000    0.041    0.000 {method 'remove' of 'list' objects}
"""

"""
Очень тяжелый код. Видимо из-за двух функций, нахождени 50 и 500 простого числа занимает уже msec."""