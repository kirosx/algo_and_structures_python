#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random
a=[random.choice([i for i in range(100)]) for k in range(10)]
print(f'Массив случайных чисел:\n{a}')
min_index = a.index(min(a))
max_index = a.index(max(a))
a[min_index], a[max_index] = a[max_index], a[min_index]
#Почему не работает так?
#a[a.index(min(a))], a[a.index(max(a))] = a[a.index(max(a))], a[a.index(min(a))]
print(f'Поменяли min и max элементы местами:\n{a}')
