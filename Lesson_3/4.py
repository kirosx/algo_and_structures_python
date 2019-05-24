# 4.	Определить, какое число в массиве встречается чаще всего.
import random
a = [random.choice([i for i in range(8)]) for k in range(40)]
print(f'массив случайных чисел:\n{a}')
number = None
max_count = 0
for i in a:
 if a.count(i)>max_count:
  max_count, number = a.count(i), i
print(f'Самое частое число - {i}, встречается {max_count} раз')
