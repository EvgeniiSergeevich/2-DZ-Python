# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 6782 -> 23
# - 0,56 -> 11

x = float(input('Введите число: '))
sum = 0
x_string = str(x).split('.')        # Отделяю целую часть от дробной

if int(x_string[1]) == 0:           # Получаю целое число из вещественного(123.51 -> 12351)
    x = int(x_string[0])
else:
    x = int (x * 10 ** len(x_string[1]))

for i in range(len(str(x))):        # Вычисляю сумму цифр
    sum  += x % 10
    x //= 10
print('sum = ', sum)