# Сумма последовательсноти
# Задайте список из n чисел последовательности (1+ 1/n)**n и выведите на экран их сумму.
# Например, для n = 4 последовательность будет иметь вид [2.0, 2.25, 2.37037037037037, 2.44140625]
# сумма будет равна 9.06177...
# Input format
# На вход поступает одно целое число
# Output format
# Одно число, сумма последовательности.

n = int(input())
sum = 0
for i in range(1, n+1):
    i=(1 + 1/i) ** i
    sum += i
print (sum)