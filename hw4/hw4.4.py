# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('k = '))
kefs = list(randint(0,100) for i in range(k+1))
# kefs = list(map(int, input().split())) # для проверки коэф. многочлена равных 0 или 1
print(kefs)
if kefs[0] != 0:
    polynom = str(kefs[0])+' = 0'
else:
    polynom = ' = 0' # если константа многочлена равна 0
if k > 0 and kefs[1] > 1: # если коэф. члена х неравен 0. Например при ax^2 + bx + c = 0; b = 0
    polynom = str(kefs[1])+'x + '+polynom
    if k > 1:
        for i in range(2, k+1):
            if kefs[i] > 1:
                polynom = str(kefs[i])+'x^'+str(i)+' + ' + polynom
            elif kefs[i] == 1: # если коэф. члена х^i равен 1. Например при ax^2 + bx + c = 0; a = 1
                polynom = 'x^'+str(i)+' + ' + polynom
            else:
                i+=1
elif k > 0 and kefs[1] == 0: # если коэф. члена х равен 0. Например при ax^2 + bx + c = 0; b = 0
    if k > 1:
        for i in range(2, k+1):
            if kefs[i] > 1:
                polynom = str(kefs[i])+'x^'+str(i)+' + ' + polynom
            elif kefs[i] == 1:
                polynom = 'x^'+str(i)+' + x + ' + polynom
            else:
                i+=1
elif k > 0 and kefs[1] == 1: # если коэф. члена х равен 1. Например при ax^2 + bx + c = 0; b = 1
    if k > 1:
        for i in range(2, k+1):
            if kefs[i] > 1:
                polynom = str(kefs[i])+'x^'+str(i)+' + ' + polynom
            elif kefs[i] == 1:
                polynom = 'x^'+str(i)+' + x + ' + polynom
            else:
                i+=1
print(polynom)