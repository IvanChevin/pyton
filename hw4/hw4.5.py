# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('hw4\hw4.5_1.txt', 'r') as file_1:
    mult_1 = str(*file_1)
with open('hw4\hw4.5_2.txt', 'r') as file_2:
    mult_2 = str(*file_2)

mult_1=mult_1[0:-4]
mult_2=mult_2[0:-4]

mult_res = mult_1 + ' + ' + mult_2 + ' = 0'

with open('hw4\hw4.5_result.txt', 'w') as file_res:
    file_res.write(mult_res)
