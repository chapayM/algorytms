"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
 для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
 и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""

from collections import namedtuple


Firm = namedtuple("Firm", ["name", "profit"])
firms = []
total_profit = 0
count = int(input("Количество предприятий "))
for _ in range(count):
    name = input("Наименование предприятия ")
    profit = int(input("Годовой доход "))
    firms.append(Firm(name=name, profit=profit))
    total_profit = total_profit + profit
    _ += 1
profit_mediana = total_profit / count

print(f"Предприятия с прибылью выше средней {profit_mediana}: ")
for Firm in firms:
    if Firm.profit >= profit_mediana:
        print(f"{Firm.name} - {Firm.profit}")
print(f"Предприятия с прибылью ниже средней {profit_mediana}: ")
for Firm in firms:
    if Firm.profit < profit_mediana:
        print(f"{Firm.name} - {Firm.profit}")



