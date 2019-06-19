# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
num = [i for i in range(2,10)]
allnum = [i for i in range(2,100)]
res = {}
for i in num:
 res[i]=0
 for k in allnum:
  if k%i==0:
   res[i]+=1
for k,v in res.items():
 print(f'Число {k}, кратных ему чисел {v}')

