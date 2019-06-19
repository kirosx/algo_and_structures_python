"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
import random
a = [random.choice([i for i in range(20)]) for k in range(20)]
print(f'Массив:\n{a}')
min1 = a.pop(a.index(min(a)))
min2 = a.pop(a.index(min(a)))
print(f'Два минимальных числа:\n{min1}\n{min2}')
