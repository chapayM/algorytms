# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число. Проанализировать скорость
# и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых
# уроков. Используйте этот код и попробуйте его улучшить/оптимизировать
# под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
import cProfile

#Метод Решето Эратосфена

# def prime_number(i):
#     n = i
#     m = 0
#     result_list = []
#     num_array = []
#     while len(result_list)!=i:
#         num_array += [x for x in range(len(num_array), len(num_array)+i-len(result_list))]
#         for j in range(2, m+i-len(result_list)):
#             if num_array[j] != 0:
#                 k = j * 2
#                 while k<n:
#                     num_array[k] = 0
#                     k += j
#         result_list = [x for x in num_array if x!=0 and x!=1]
#         m = len(num_array)
#         n += i - len(result_list)
#     return result_list[-1]

# prime_number(5)
# 1000 loops, best of 5: 9.03 usec per loop
# 59 function calls in 0.000 seconds

# prime_number(50)"
# 1000 loops, best of 5: 424 usec per loop
# 185 function calls in 0.000 seconds

# prime_number(100)
# 1000 loops, best of 5: 2.49 msec per loop
# 365 function calls in 0.003 seconds


def prime_number(i):
    result_list=[2]
    j = 2
    while len(result_list)!=i:
        for n in range(2, j):
            if j%n == 0:
                break
            elif n==j-1:
                result_list.append(j)
        j += 1
    return result_list[-1]

# prime_number(5)
# 1000 loops, best of 5: 2.93 usec per loop
# 19 function calls in 0.000 seconds
#  11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# prime_number(50)
# 1000 loops, best of 5: 257 usec per loop
# 282 function calls in 0.001 seconds
# 229    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 49    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# prime_number(100)
# 1000 loops, best of 5: 1.32 msec per loop
# 644 function calls in 0.002 seconds

#prime_number(500)
# 1000 loops, best of 5: 50.2 msec per loop
# 4074 function calls in 0.051 seconds
# 3571    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}



# cProfile.run("prime_number(100)")

# Выводы: Оба алгоритма расчета простого числа по заданному номеру резко
# увеличивают потребности в ресурсах с ростом позиции. При этом метод
# простого перебора лучше оптимизирован для Python и является примерно в 2 раза более быстрым.
