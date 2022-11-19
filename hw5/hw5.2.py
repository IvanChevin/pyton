# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random

def pvp():
  candies_on_table = 2021
  candies_for_step = 28
  count = 0
  while candies_on_table > 0:
    if count == 0:
      step = int(input('Ходит Игрок 1. Введи количество конфет: '))
      if step > candies_for_step or step > candies_on_table:
        step = int(input('Слишком много! Возьми меньше: '))
      candies_on_table = candies_on_table - step
    if candies_on_table > 0:
      print(f'на столе еще {candies_on_table} конфет!')
      count = 1
    else:
      print('Конфеты закончились! Победил Игрок 1!')

    if count == 1:
      step = int(input('Ходит Игрок 2. Введи количество конфет: '))
      if step > candies_for_step or step > candies_on_table:
        step = int(input('Слишком много! Возьми меньше: '))
      candies_on_table -= step
    if candies_on_table > 0:
      print(f'на столе еще {candies_on_table} конфет!')
      count = 0
    else:
      print('Конфеты закончились! Победил Игрок 2!')
  
def pve():
  candies_on_table = 2021
  candies_for_step = 28
  players = ['Игрок','Компьютер']
  mover = random.randint(-1, 0)
  print(f'Первым ходит {players[mover+1]}!')

  while candies_on_table > 0:
    mover += 1

    if players[mover % 2] == 'Компьютер':
      if candies_on_table < 29:
        step = candies_on_table
      else:
        step = candies_on_table % (candies_for_step + 1)
        if step == 0:
          step = random.randint(1, candies_for_step)
        # delenie = candies_on_table // candies_for_step
        # step = candies_on_table - (delenie * candies_for_step + 1)
      print(f'Компьютер забирает {step} конфет')

    else:
      step = 0
      while step < 1 or step > 28:
        step = int(input('Введи количество конфет: '))
        if step > candies_for_step or step > candies_on_table:
          step = int(input('Слишком много! Возьми меньше: '))
        if step == 0:
          step = int(input('Ты должен взять хотябы одну конфетку: '))
        
    candies_on_table = candies_on_table - step
    if candies_on_table > 0:
      print(f'на столе еще {candies_on_table} конфет!')
    else:
      print(f'Конфеты закончились! Победил {players[mover % 2]}!')
  
print("""1. Игрок против игорока
2. Игрок против компьютера""")
mode = 0
while mode != 1 or mode != 2:
  if mode == 1:
    print(pvp())
    exit()
  elif mode == 2:
    print(pve())
    exit()
  else:
    mode = int(input('Введите 1 или 2 чтобы выбрать режим: '))

