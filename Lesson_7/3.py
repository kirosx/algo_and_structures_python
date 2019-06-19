"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
import random

array = [random.randint(0,100) for i in range(random.randint(10,20)*2+1)]
print(f'Исходный массив:\n{array}')
for i in range(len(array)):
 equals=[]
 for x in range(len(array)):
  if array[x]!=array[i]:
   equals.append('l') if array[x]>array[i] else equals.append('g')
 if equals.count('l')==equals.count('g'):
  print(f'Медиана массива - элемент {array[i]}')
  break
