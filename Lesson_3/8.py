"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
from pprint import pprint
matrix = []
for i in range(4):
 matrix.append([int(i) for i in input(f'Введите 4 вектора матрицы числа через пробел(вектор{i+1}):\n').split(' ')])
matrix.append([sum(matrix[0]),sum(matrix[1]),sum(matrix[2]),sum(matrix[3])])
print(f'Полученная матрица:\n')
pprint(matrix)
