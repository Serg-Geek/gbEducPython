# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

def input_int_in_range(start, end):
    while True:
        try:
            n = int(input("Введите числовое значение дня недели от 1 до 7: "))            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if start <= n <= end:
                return n
            print("Введённое число вне диапазона")%(start, end)

day=input_int_in_range(1, 7)
if day<6:
    print("->NO")
else: print("->YES")