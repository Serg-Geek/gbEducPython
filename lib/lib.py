


def input_float():
    while True:
        try:
            n = float(input("Введите число: ")) 
            return n            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    


def input_int():
    while True:
        try:
            n = int(input("Введите число: ")) 
            return n            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.") 

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


nums = input("Введите список чисел, разделенных пробелом: ").split()

num=input_int()
num_list=[]
for i in range(1, num+1):
    num_list.append(i)