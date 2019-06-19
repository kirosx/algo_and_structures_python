"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
import random

def merge_sorting(array):
 if len(array)<2:
  return array
 left = merge_sorting(array[:len(array)//2])
 right = merge_sorting(array[len(array)//2:len(array)])
 i = j = 0
 sorted_array = []
 while i<len(left) or j<len(right):
  if i>=len(left):
   sorted_array.append(right[j])
   j+=1
  elif j>=len(right):
   sorted_array.append(left[i])
   i+=1
  elif left[i]<right[j]:
   sorted_array.append(left[i])
   i+=1
  else:
   sorted_array.append(right[j])
   j+=1
 return sorted_array

random_float_array = [random.uniform(0,50) for i in range(random.randint(10,20))]

print(f'''Случайный массив вещественных чисел:
{random_float_array}
Отсортированный слиянием:
{merge_sorting(random_float_array)}''')
