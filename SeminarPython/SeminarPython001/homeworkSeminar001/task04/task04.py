# Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).


import numbers


def input_int_in_range():
    while True:
        try:
            n = int(input("Введите № четверти, от 1 до 4: "))            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if  0< n <5:
                return n
            print("Введённое число вне диапазона: ")

number = input_int_in_range()
if number == 1: 
    print("диапазон возможных координат x>0 and y>0")
elif number == 2:
    print("диапазон возможных координат x>0 and y<0")
elif number == 3:
    print("диапазон возможных координат x<0 and y<0")
else:
    print("диапазон возможных координат x<0 and y>0")
