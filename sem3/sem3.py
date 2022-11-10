#реализуйте генератор целых случайных чисел
from datetime import datetime
# def rand(seed):
#     now = datetime.now()
#     print
#     #return now.day*now.month/now.year*seed
now = str(datetime.now())
x = int(now[-4:-1])
print(x)
