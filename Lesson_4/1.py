"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
from timeit import timeit

n = 1234567890

def odd_even(n):
 even_count = 0
 odd_count = 0
 while n>0:
  if n%10%2==0:
   even_count+=1 
  else:
   odd_count+=1
  n//=10
 return even_count, odd_count

#Заменим цикл While на For
def odd_even_for(n):
 even_count = 0
 odd_count = 0
 l = len(str(n))
 for i in range(l):
  if n%10%2==0:
   even_count+=1 
  else:
   odd_count+=1
  n//=10
 return even_count, odd_count

#Определение поэлементно
def count_with_string(n):
 odds=0
 evens=0
 string = str(n)
 for i in string:
  if int(i)%2==0:
   evens+=1
  else:
   odds+=1
 return evens, odds

#Рекурсия

def odd_even_rec(n,odds=0,evens=0):
 if n==0:
  return odds, evens
 if n%10%2==0:
  evens+=1
  return odd_even_rec(n//10,odds,evens)
 else:
  odds+=1
  return odd_even_rec(n//10,odds,evens)

while_time=timeit('odd_even(n)', setup='from __main__ import n, odd_even')
for_time=timeit('odd_even_for(n)', setup='from __main__ import n, odd_even_for')
rec_time=timeit('odd_even_rec(n)', setup='from __main__ import n, odd_even_rec')
str_time=timeit('count_with_string(n)', setup='from __main__ import n, count_with_string')
print(f'''Выполнение с циклом while заняло {while_time} сек.
Выполнение с циклом for заняло {for_time} сек.
Выполнение рекурсивно заняло {rec_time} сек.
Итерация по строке заняла {str_time} сек.''')
 
#Цикл с while показывает лучшие результаты
