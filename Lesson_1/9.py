# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

a = float(input('Введите три разных числа:\n'))
b = float(input())
c = float(input())
m = 'среднего числа нет'
if b<a<c or c<a<b:
 m = a
elif a<b<c or c<b<a:
 m = b 
elif a<c<b or b<c<a:
 m = c 
print(f'среднее число: {m}')
