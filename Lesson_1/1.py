# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

three_digit_number = int(input('Введите трёхзначное число:'))
hundreds = three_digit_number//100
dozens = three_digit_number//10%10
units = three_digit_number%10
print(f'сумма цифр цисла = {hundreds+dozens+units}\nпроизведение цифр числа = {hundreds*dozens*units}')
