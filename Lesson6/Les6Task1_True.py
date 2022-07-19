import sys
from random import randint
import max_negative_num1
import max_negative_num2
import max_negative_num3

def get_variables(ret_names=False):
    return [v if not ret_names else i for i, v in globals().items() if
            not i.startswith('_') and not hasattr(v, '__name__')]


# Расчёт выделеной памяти
def calc_memory():
    _processed = set()  # список для хранения уже обработанных адресов памяти

    def _get_size(object):
        object_id = id(object)
        if object_id in _processed:  # Проверим не обрабатывали ли мы этот адрес памяти
            return 0  # Нет смысла суммировать уже обработанный адрес
        size = sys.getsizeof(object)
        _processed.add(object_id)
        if hasattr(object, '__iter__') and not isinstance(object, str):
            if hasattr(object, 'items'):  # Проверка на словаль типа ключ-значение
                size += sum(_get_size(k) + _get_size(v) for k, v in getattr(object, 'items')())
            else:
                size += sum(_get_size(v) for v in object)
        return size

    return _get_size(get_variables()) # Запуск на первом цикле с рекурсией для определения пречня пременных


print(sys.version, sys.platform)
#3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] win32
list1 = [randint(-10, 10) for _ in range(10)]


print('*' * 100)
print('Варинат 1')
ver1_var = max_negative_num1.max_negative_number1(list1)
print('Затраты памяти: %s' % calc_memory())
print('Переменные', get_variables(True))
print('Значения переменных:', get_variables(), sep="\n")
del ver1_var


print('*' * 100)
print('Варинат 2')
ver2_var = max_negative_num2.max_negative_number2(list1)
print('Затраты памяти: %s' % calc_memory())
print('Переменные', get_variables(True))
print('Значения переменных:', get_variables(), sep="\n")
del ver2_var

print('*' * 100)
print('Варинат 3')
ver3_var = max_negative_num3.max_negative_number3(list1)
print('Затраты памяти: %s' % calc_memory())
print('Переменные', get_variables(True))
print('Значения переменных:', get_variables(), sep="\n")
del ver3_var
