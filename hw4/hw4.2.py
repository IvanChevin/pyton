# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('N = '))
devisors = []
devisor = 2
while devisor <= N:
    if N % devisor == 0:
        devisors.append(devisor)
        N /= devisor
    else:
        devisor+=1
print(*devisors)
