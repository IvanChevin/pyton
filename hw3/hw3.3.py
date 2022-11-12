# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_n = list(map(float, input().split()))
for i in range (len(list_n)):
    list_n[i] = round(list_n[i] % 1, 3)
    print(list_n[i])
print(max(list_n) - min(list_n))