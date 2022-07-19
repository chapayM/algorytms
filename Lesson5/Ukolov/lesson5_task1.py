# -*- coding: utf-8 -*-
"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
import collections
Firm = collections.namedtuple('Firm', ['firm_name', 'profit'])
n = int(input('Количество фирм: '))
firm_list = []
average_profit = 0
for i in range(n):
    firm_list.append(Firm(input("Название фирмы: "), float(input("Прибыль за год: "))))
    average_profit += firm_list[-1].profit
average_profit /= n
print(f"Средняя прибыль: {average_profit}")
list_above = []
list_below = []
for i in range(n):
    if firm_list[i].profit >= average_profit:
        list_above.append(firm_list[i].firm_name)
    else:
        list_below.append(firm_list[i].firm_name)
print(f"Фирмы с прибылью выше средней: {list_above}")
print(f"Фирмы с прибылью ниже средней: {list_below}")
