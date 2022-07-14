# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import defaultdict
from statistics import mean

corp = defaultdict(int)
for _ in range(int(input('Введите количество предприятий: '))):
    corp_name = input("Введите назнание компании: ")
    for el in ['1q', '2q', '3q', '4q']:
        corp[corp_name] += int(input(f'Введите прибыль компании за {el}: '))

print(corp)
print(f'Средняя годовая прибыль: {mean(corp.values())}')
print(f"Выше среднего прибыль у следующих компаний: {[el for el in corp if corp[el]>mean(corp.values())]}")
print(f"Ниже среднего прибыль у следующих компаний: {[el for el in corp if corp[el]<mean(corp.values())]}")

