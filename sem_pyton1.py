# a=3
# b=3.4
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a//b)
# print(a%b)

# Задача 1
# Напишите программу, которая принимает на вход два 
# числа и проверяет, является ли одно число квадратом другого.
# Да. Нет

# a=int(input("a = "))
# b=int(input("a = "))
# if a*a==b:
#     print("да")
# elif b*b==a:
#     print("да")
# else:
#     print("нет")

# a=[int(i) for i in input().split(' ')] #list comprehension
# b=list(map(int,input().split()))#обычный ввод списка с изменением
# names=input().split(',')#ввод списка с клавиаутры БЕЗ ИЗМЕНЕНИЙ ЕГО ЭЛЕМЕНТОВ

# https://docs.python.org/3/ # документация по питону

# Задача 2
# Напишите программу, которая будет на вход принимать
#  число N и выводить числа от -N до N

N=int(input("N = "))
for i in range(-N,N+1):
    print(i)


