"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
a = [random.choice([i for i in range(100)]) for k in range(20)]
print(f'массив:\n{a}\n')
min_elem = a.index(min(a))
max_elem = a.index(max(a))
print(f'Сумма чисел между {min(a)} и {max(a)}:\n')
print(sum(a[min_elem+1:max_elem])) if min_elem<max_elem else print(sum(a[max_elem+1:min_elem]))
