# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text_str = 'абв парампампам абвегд прампампам'
text_list = text_str.split()
for i in range(len(text_list)-2):
    if 'абв' in text_list[i]:
        del text_list[i]
print(*text_list)