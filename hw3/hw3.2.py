# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_n = list(map(int, input().split()))
list_m = list()
sum = 0
for i in range((len(list_n)+1)//2):
    sum = list_n[i] * list_n[len(list_n)-1-i]
    list_m.append (sum)
print(list_m)