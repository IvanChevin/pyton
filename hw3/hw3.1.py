# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_n = list(map(int, input().split()))
sum = 0
for i in range(1, len(list_n), 2):
    sum += list_n[i]
print(sum)

