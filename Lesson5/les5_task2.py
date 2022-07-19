# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
# представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы счисления
# в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import deque
import timeit


def sum_hex(a, b):
    number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    result = deque()
    i = 0
    while a != deque([]) or b != deque([]) or i != 0:
        try:
            summand1 = a.pop()
        except IndexError:
            summand1 = '0'
        try:
            summand2 = b.pop()
        except IndexError:
            summand2 = '0'
        if number.index(summand1) + number.index(summand2) + i <= 15:
            result.appendleft(number[number.index(summand1) + number.index(summand2) + i])
            i = 0
        else:
            result.appendleft(number[number.index(summand1) + number.index(summand2) - 16 + i])
            i = 1
    return deque(result)


def mul_hex(a, b):
    number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    if b == deque(['0']):
        return deque(['0'])
    else:
        result = a.copy()
        i = 0
        b_dec = 0
        b.reverse()
        for el in b:
            b_dec += number.index(el) * 16 ** i
            i += 1
        for _ in range(b_dec - 1):
            result = sum_hex(a.copy(), result.copy())
        return deque(result)


# num1 = deque(input('Введите первое число: '))
# num2 = deque(input('Введите второе число: '))
num1 = deque(['A', '2'])
num2 = deque(['A', '2'])
# operation = input('Введите операцию которую вы хотите произвести + или *: ')
# if operation == '+':
print(sum_hex(num1.copy(), num2.copy()))
# elif operation == "*":
print(mul_hex(num1, num2))
# else:
#     print('Знак операции неверный!')
