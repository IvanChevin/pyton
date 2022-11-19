# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text_str = 'абв парампампам абвегд прампампам'
text_list = text_str.split()
for i in range(len(text_list)-2):
    if 'абв' in text_list[i]:
        if not text_list[i].isidentifier():
            text_list[i] = text_list[i][-1]
        # del text_list[i]
        else:
            text_list[i] = ''
print(*text_list)