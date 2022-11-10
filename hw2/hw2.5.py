# Перемешивание
# Считайте элементы и сформируйте из него список. Реализуйте следующий алгоритм перемешивания 
# списка: Необходимо пройтись по всем элемента от 0 до последнего один раз и каждый четный элемент 
# поменять местами с предыдущим, каждый нечетный со следующим, если такое возможно.
# Input format
# Целые числе через пробел
# Output format
# Целые числе через пробел

# n = list(map(int, input().split()))
# temp = 0
# for i in range(len(n)):
#     if i % 2 == 0 and i > 0:
#         # temp = n[i]
#         # n[i] = n[i - 1]
#         # n[i - 1] = temp
#         n[i], n[i-1] = n[i-1], n[i]
#     elif i % 2 != 0 and i + 1 < len(n):
#         # temp = n[i]
#         # n[i] = n[i + 1]
#         # n[i + 1] = temp
#         n[i], n[i+1] = n[i+1], n[i]
#     print(n)
# print(*n)

i = [int(x) for x in input().split()]
for j, item in enumerate(i):
    if item % 2 == 0 and j > 0:
        i[j], i[j-1] = i[j-1], i[j]
    elif item % 2 != 0 and j < len(i)-1:
        i[j], i[j+1] = i[j+1], i[j]
    print(i)
print(*i, sep=" ", end="")