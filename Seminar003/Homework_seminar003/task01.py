# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def input_int():
    while True:
        try:
            n = int(input("Введите число: ")) 
            return n            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.") 

num=input_int()
num_list=[]
for i in range(1, num+1):
    num_list.append(random.randint(0,100))
print(num_list)
odds_list = num_list[1: num+1: 2]
print(odds_list)
sum_odds=0
for i in odds_list:
    sum_odds += i
print(sum_odds)