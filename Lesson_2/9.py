"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

def recursive_sum_digits(n,summ=0):
 if n==0:
  return summ
 return recursive_sum_digits(n=n//10,summ=summ+n%10)


result = 0
current_digit = 0
while True:
 digit = input('Вводите числа, для подтверждение окончания - "!":\n')
 if digit == '!':
  print(f'Лучший результат - {result} для числа - {current_digit}')
  exit()
 elif recursive_sum_digits(n=int(digit))>result:
  result = recursive_sum_digits(int(digit))
  current_digit = digit
