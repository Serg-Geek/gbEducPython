# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def input_int_in_range():
    while True:
        try:
            n = int(input("Введите число: "))            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if n !=0:
                return n
            print("Введённое число вне диапазона: ")
x = input_int_in_range()
y = input_int_in_range()
print(x,y)
if x>0 and y>0:
    print("1-Четверть")
if x>0 and y<0:
    print("2-Четверть")
if x<0 and y<0:
    print("3-Четверть")
if x<0 and y>0:
    print("4-Четверть")
