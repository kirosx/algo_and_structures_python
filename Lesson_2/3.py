"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

number = int(input('Введите число:\n'))
reversed_number = ''
while number>0:
 reversed_number+= str(number%10)
 number//=10
print(reversed_number)

#Рекурсия
def recursion_reverse(n,k=''):
 if n<10:
  k+=str(n)
  print(k)
 else:
  k+=str(n%10)
  recursion_reverse(n//10,k)

recursion_reverse(int(input('Введите число для разворота рекурсивно:\n')))
 
