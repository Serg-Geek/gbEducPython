# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры 
import random
def input_int_in_range_more_zero():
    while True:
        try:
            n = int(input("Введите число: "))            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if n > 0:
                return n
            print("Введённое число вне диапазона: ")
def input_int_in_range():
    while True:
        try:
            n = int(input("Введите число: "))            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if n >= 0:
                return n
            print("Введённое число вне диапазона: ")
num=input_int_in_range_more_zero()#>0
num_list=[]
for i in range(0, num):
    num_list.append(random.randint(-num, num))
print(num_list)
print('Введите количество элементов которые необходимо умножить')# >0
pos= input_int_in_range_more_zero()
p = 1
for i in range(pos):
    print('введите № позиции элемента начиная с 0:')#=>0    
    n= input_int_in_range()
    p=p*num_list[n]
print()    
print('Произведение элементов на указанных позициях = ', p)