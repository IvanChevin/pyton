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

# N = int(input("N = "))
# for i in range(-N, N+1):
#    print(i)

# N = int(input("N = "))
# print([i for i in range(-N, N+1)]) # задание списка циклом for

# Задача 3
# Напишите программу, которая будет принимать на вход 
# дробь и показывать первую цифру дробной части числа.

# n = float(input('Введите число N: '))
# a = int( (n*10) % 10 )
# print(a)


# Задача 4
# Напишите программу, которая принимает на вход число и 
# проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# i = int(input('i = '))
# if (i%5 == 0 and i%10 ==10) or (i%15 == 0 and not i%30 == 0):
#     print('yes')
# else:
#     print('no')

x = [i for i in range(10)] # задать список от 1 до 10
print(x)
a=[int(i) for i in input().split(' ')]
print(a)





