# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

a = input()

sum = 0
for i in a:
    try:
        ret = int(i)
    except ValueError:
            ret = 0
    sum += ret
print(sum)