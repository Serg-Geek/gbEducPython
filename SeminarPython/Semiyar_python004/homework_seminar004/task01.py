# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# !!ВНИМАНИЕ

# # !!! не использовать константу math.pi
# import random

# r= 1#радиус

# r2=r**2# площадь квадрата
# pi=0
# n=100000# Колво попроров
# x=0
# y=0
# res=0
# for n in range(n):
#     x= random.uniform(0,1)
#     y = random.uniform(0,1)
#     if (x*x+y*y) <=1:
#         res=res+1
# pi = 4*(res/n)   
# print(pi)



# n = 10


def input_int_in_range ():
    while True:
        try:
            n = int(input("Введите число знаков после запятой от 1 до 10: ")) 
                  
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
        else:
            if 1 <= n <= 10:
                return n
            print("Введённое число вне диапазона")

def get_pi(num_after_decimal_point):
    n=10**(num_after_decimal_point+2)
    pi=0
    for n in range(0,100000):
          pi=pi+((-1)**n)/(2*n+1)
    return pi*4
n=input_int_in_range()
pi = get_pi(n)
print(round(pi,n))





