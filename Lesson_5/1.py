"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import defaultdict
quart_profit = defaultdict(list)
for i in range(int(input('Введите количество предприятий, для которых необходим расчёт:'))):
 quart_profit[input('Введите название предприятия:\n')].extend(input('Введите поквартальную выручку, через пробел:\n').split(' '))
year_middle_profit = defaultdict(int)
for k,v in quart_profit.items():
 year_middle_profit[k]=sum([int(i) for i in v])/4
middle_prof = sum(year_middle_profit.values())/len(year_middle_profit.keys())
print(f'Средняя годовая выручка по предприятиям:\n{year_middle_profit}\nОбще-средняя выручка:{middle_prof}')
lower,upper=[],[]
for k,v in year_middle_profit.items():
 lower.append(k) if v<middle_prof else upper.append(k)
print(f'Компании с выручкой ниже средней:\n{lower} \n Компании с выручкой выше средней:\n{upper}')
