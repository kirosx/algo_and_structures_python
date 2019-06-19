"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

number = int(input('Введите число:\n'))
even_count = 0
odd_count = 0
while number>0:
 if number%10%2==0:
  even_count+=1 
 else:
  odd_count+=1
 number//=10
print(f'Чётных цифр: {even_count}\nНечётных цифр: {odd_count}')

#Рекурсия

def odd_even_rec(n,odds=0,evens=0):
 if n==0:
  print(f'Чётных цифр: {evens}\nНечётных цифр: {odds}')
  return
 if n%10%2==0:
  evens+=1
  odd_even_rec(n//10,odds,evens)
 else:
  odds+=1
  odd_even_rec(n//10,odds,evens)
 
odd_even_rec(int(input('Введите число для вычисления рекурсивно:\n')))
