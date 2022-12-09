import controller as cont
import name_number as name

def showinfo(a):
    print(a)



def get_numb(pr):
    if len(pr) > 0:
        print(pr)
    return int(input())
def get_str(pr):
    if len(pr) > 0:
        print(pr)
    a = str(input())
    return a

def get_numb_menu(c):
    print(c)
    while True:
        try:
            n = int(input("Введите числовое значение от 0 до 9: "))            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if 0 <= n <= 9:
                return n
            print("Введённое число вне диапазона")

def print_dct(dct):
    for key,value in dct.items(): print(key, '.  ', value)

def print_dct_value(dct):
    for value in dct.values(): print(value)

def result_page(l):
    if len(l)>0:
        for st in l:
            print(st)
    else:
        print('Not found')

    
