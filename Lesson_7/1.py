"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
import random

def bubble_sorting(array):
 for i in range(len(array)-1):
  for x in range(len(array)-1-i):
   if array[x]>array[x+1]:
    array[x], array[x+1] = array[x+1], array[x]
 return array

random_array = [random.randint(-100,100) for i in range(random.randint(10,20))]
print(f'''Массив случайных чисел, случайного размера:
{random_array}
Отсортированный массив:
{bubble_sorting(random_array)}''')

