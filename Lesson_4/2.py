"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
from timeit import timeit

n=100
def prime_or_not(number):
 for i in range(2, int(number**0.5)+1):
  if number % i == 0:
   return False
 return True

def what_prime(number):
 a=[]
 i=1
 while len(a)<=number:
  if prime_or_not(i):
   a.append(i)
  i+=1
 return a[-1]

time_no_er=timeit('what_prime(n)',setup='from __main__ import n, what_prime, prime_or_not', number=1000)
print(f'Вычисление простого числа без решета {time_no_er} сек')

def eratosphen(n):
 a = [i for i in range(n+1)]
 a[1] = 0
 lst = []
 i = 2
 while i<=n:
  if a[i] !=0:
   lst.append(a[i])
   for j in range(i,n+1,i):
    a[j]=0
  i+=1
 return(lst)

def prime_with_eratosphen(n):
 i=2
 while len(eratosphen(i))<n:
  i+=1
 return eratosphen(i)[-1]
    
time_with_er=timeit('prime_with_eratosphen(n)', setup='from __main__ import n, prime_with_eratosphen',number=1000)
print(f'С решетом {time_with_er} сек')

#Вычисление простого числа с решетом Эратосфена заняло в 75.5379707852166 больше времени
