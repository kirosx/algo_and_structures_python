# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from pprint import pprint
import random
matr=[]
for i in range(5):
 matr.append([random.choice([i for i in range(20)]) for k in range(5)])
print(f'Сформируем матрицу случайных чисел 5х5:\n')
pprint(matr)
matr_rev = []
for i in range(5):
 matr_rev.append([b[i] for b in matr])
print(f'Получим столбцы этой матрицы:\n{matr_rev}')
print(f'Список из минимальных элементов столбцов:\n{[min(i) for i in matr_rev]}')
print(f'Максимальный элемент среди них:\n{max([min(i) for i in matr_rev])}')
