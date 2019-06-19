"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

import random
digit = random.randint(0,100)
attempt = 10
while attempt!=0:
 ans = int(input(f'(осталось {attempt} попыток)\nВведите загаданное число:'))
 if ans == digit:
  print('Поздравляю вы выйграли!')
  exit()
 print('Число БОЛЬШЕ') if ans<digit else print('Число МЕНЬШЕ')
 attempt-=1
print(f'У вас закончились попытки( загаданное число: {digit}')
