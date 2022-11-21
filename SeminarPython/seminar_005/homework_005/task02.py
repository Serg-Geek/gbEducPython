# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
from random import randint
def input_int_in_range():
    while True:
        try:
            n = int(input("Введите числовое значение дня недели от 1 до 28: "))            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if 1 <= n <= 28:
                return n
            print("Введённое число вне диапазона")
candy=2021  
player_1 = input(' input name 1: ')
player_2 =input(' input name 2: ')

flag = randint(0,2)
def game():
    candy = candy - input_int_in_range()
    return candy

while candy > 28:
    if flag:
        
        print(player_1)
        candy = candy - input_int_in_range()
        flag = False
        print('remaining candy', candy)
    else:
        print(player_2)
        candy = candy - input_int_in_range()
        flag = True
        print('remaining candy', candy)
if flag:
    print(f"Выиграл {player_1}")
else:
    print(f"Выиграл {player_2}")







