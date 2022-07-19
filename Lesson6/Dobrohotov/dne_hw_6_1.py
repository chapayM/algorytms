import sys

def show_size(x, level=0):
    print('\t' * level,
          f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)





from collections import OrderedDict
dict = OrderedDict()
list_more = []
list_less = []
sum = 0
try:
    while True:
        n = input('Введите количество предприятий (целое число): ')
        if n.isdigit() == True:
            break
    for i in range(0, int(n)):
        a = input(f'Введите название {i+1} предприятия:')
        b = input(f'Введите прибыль за четыре квартала {i+1} предприятия:')
        sum += int(b)
        dict[a] = b
    average = sum / int(n)
    print(f'Для {n} предприятий средняя прибыль равна ${average} ')
    for el in dict:

        if int(dict[el]) <= average:
            list_less.append(el)
        else:
            list_more.append(el)
    print()
    print(f'Предприятия, заработавшие больше среднего: {list_more}')
    print('*' *50)
    print(f'Предприятия, заработавшие мельше среднего: {list_less}')
except:
    print('Ошибка! Попробуйте другие значения')


print('dict', end='')
show_size(dict)
print('list_more', show_size(list_more))
print('list_less', show_size(list_less))
print('sum', show_size(sum))
print('n', show_size(n))
print('a', show_size(a))
print('b', show_size(b))
print('average', show_size(average))

# Результат запуска программы и измерения:

# Введите количество предприятий (целое число): 2
# Введите название 1 предприятия:ООО "Рога и копыта"
# Введите прибыль за четыре квартала 1 предприятия:15000
# Введите название 2 предприятия:ООО "Ромашка"
# Введите прибыль за четыре квартала 2 предприятия:14000
# Для 2 предприятий средняя прибыль равна $14500.0
#
# Предприятия, заработавшие больше среднего: ['ООО "Рога и копыта"']
# **************************************************
# Предприятия, заработавшие мельше среднего: ['ООО "Ромашка"']
#  type= <class 'collections.OrderedDict'>, size= 424, object= OrderedDict([('ООО "Рога и копыта"', '15000'), ('ООО "Ромашка"', '14000')])
# 	 type= <class 'tuple'>, size= 56, object= ('ООО "Рога и копыта"', '15000')
# 		 type= <class 'str'>, size= 112, object= ООО "Рога и копыта"
# 		 type= <class 'str'>, size= 54, object= 15000
# 	 type= <class 'tuple'>, size= 56, object= ('ООО "Ромашка"', '14000')
# 		 type= <class 'str'>, size= 100, object= ООО "Ромашка"
# 		 type= <class 'str'>, size= 54, object= 14000
# dict None
#  type= <class 'list'>, size= 88, object= ['ООО "Рога и копыта"']
# 	 type= <class 'str'>, size= 112, object= ООО "Рога и копыта"
# list_more None
#  type= <class 'list'>, size= 88, object= ['ООО "Ромашка"']
# 	 type= <class 'str'>, size= 100, object= ООО "Ромашка"
# list_less None
#  type= <class 'int'>, size= 28, object= 29000
# sum None
#  type= <class 'str'>, size= 50, object= 2
# n None
#  type= <class 'str'>, size= 100, object= ООО "Ромашка"
# a None
#  type= <class 'str'>, size= 54, object= 14000
# b None
#  type= <class 'float'>, size= 24, object= 14500.0
# average None
#  type= <class 'str'>, size= 100, object= ООО "Ромашка"

# Process finished with exit code 0


# Введите количество предприятий (целое число): 3
# Введите название 1 предприятия:ООО "Гладиолус"
# Введите прибыль за четыре квартала 1 предприятия:17000
# Введите название 2 предприятия:АНО "Неизученные реалии"
# Введите прибыль за четыре квартала 2 предприятия:15000
# Введите название 3 предприятия:ОАО "Автосервис"
# Введите прибыль за четыре квартала 3 предприятия:14000
# Для 3 предприятий средняя прибыль равна $15333.333333333334
#
# Предприятия, заработавшие больше среднего: ['ООО "Гладиолус"']
# **************************************************
# Предприятия, заработавшие мельше среднего: ['АНО "Неизученные реалии"', 'ОАО "Автосервис"']
#  type= <class 'collections.OrderedDict'>, size= 456, object= OrderedDict([('ООО "Гладиолус"', '17000'), ('АНО "Неизученные реалии"', '15000'), ('ОАО "Автосервис"', '14000')])
# 	 type= <class 'tuple'>, size= 56, object= ('ООО "Гладиолус"', '17000')
# 		 type= <class 'str'>, size= 104, object= ООО "Гладиолус"
# 		 type= <class 'str'>, size= 54, object= 17000
# 	 type= <class 'tuple'>, size= 56, object= ('АНО "Неизученные реалии"', '15000')
# 		 type= <class 'str'>, size= 122, object= АНО "Неизученные реалии"
# 		 type= <class 'str'>, size= 54, object= 15000
# 	 type= <class 'tuple'>, size= 56, object= ('ОАО "Автосервис"', '14000')
# 		 type= <class 'str'>, size= 106, object= ОАО "Автосервис"
# 		 type= <class 'str'>, size= 54, object= 14000
# dict None
#  type= <class 'list'>, size= 88, object= ['ООО "Гладиолус"']
# 	 type= <class 'str'>, size= 104, object= ООО "Гладиолус"
# list_more None
#  type= <class 'list'>, size= 88, object= ['АНО "Неизученные реалии"', 'ОАО "Автосервис"']
# 	 type= <class 'str'>, size= 122, object= АНО "Неизученные реалии"
# 	 type= <class 'str'>, size= 106, object= ОАО "Автосервис"
# list_less None
#  type= <class 'int'>, size= 28, object= 46000
# sum None
#  type= <class 'str'>, size= 50, object= 3
# n None
#  type= <class 'str'>, size= 106, object= ОАО "Автосервис"
# a None
#  type= <class 'str'>, size= 54, object= 14000
# b None
#  type= <class 'float'>, size= 24, object= 15333.333333333334
# average None


#
# Process finished with exit code 0

# Введите количество предприятий (целое число): 1
# Введите название 1 предприятия:ОАО "Черемуха"
# Введите прибыль за четыре квартала 1 предприятия:55555
# Для 1 предприятий средняя прибыль равна $55555.0
#
# Предприятия, заработавшие больше среднего: []
# **************************************************
# Предприятия, заработавшие мельше среднего: ['ОАО "Черемуха"']
#  type= <class 'collections.OrderedDict'>, size= 392, object= OrderedDict([('ОАО "Черемуха"', '55555')])
# 	 type= <class 'tuple'>, size= 56, object= ('ОАО "Черемуха"', '55555')
# 		 type= <class 'str'>, size= 102, object= ОАО "Черемуха"
# 		 type= <class 'str'>, size= 54, object= 55555
# dict None
#  type= <class 'list'>, size= 56, object= []
# list_more None
#  type= <class 'list'>, size= 88, object= ['ОАО "Черемуха"']
# 	 type= <class 'str'>, size= 102, object= ОАО "Черемуха"
# list_less None
#  type= <class 'int'>, size= 28, object= 55555
# sum None
#  type= <class 'str'>, size= 50, object= 1
# n None
#  type= <class 'str'>, size= 102, object= ОАО "Черемуха"
# a None
#  type= <class 'str'>, size= 54, object= 55555
# b None
#  type= <class 'float'>, size= 24, object= 55555.0
# average None
#
# Process finished with exit code 0

# Введите количество предприятий (целое число): 0
# Ошибка! Попробуйте другие значения
#  type= <class 'collections.OrderedDict'>, size= 128, object= OrderedDict()
# dict None
#  type= <class 'list'>, size= 56, object= []
# list_more None
#  type= <class 'list'>, size= 56, object= []
# list_less None
#  type= <class 'int'>, size= 24, object= 0
# sum None
#  type= <class 'str'>, size= 50, object= 0
# n None

"""
Выводы:
1. Из всех использованных конструкций больше всего памяти при выполнении программы требует OrderDict.
2. Объем требуемой памяти для OrderDict увеличивается линейно при увеличении количества элементов. "Пустая колнструкция занимает 128.
3. Список может требовать меньше памяти, чем занимает объект, на который ссылается список. 
type= <class 'list'>, size= 88, object= ['ОАО "Черемуха"']
 	 type= <class 'str'>, size= 102, object= ОАО "Черемуха"
"""