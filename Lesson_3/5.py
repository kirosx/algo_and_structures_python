#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
import random
a = [random.choice([i for i in range(-10,5)]) for k in range(8)]
print(f'Массив:\n{a}')
max_neg = max([i for i in a if i<0])
print(f'Максимальное отрицательное число:{max_neg}\n позиция в массиве {a.index(max_neg)}')
