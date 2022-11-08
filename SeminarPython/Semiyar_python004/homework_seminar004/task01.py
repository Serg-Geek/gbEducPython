# Вычислить число Пи c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# !!ВНИМАНИЕ

# # !!! не использовать константу math.pi


#метод монте-карло

# import random
# pi=0
# n=1000000# Колво попроров
# x=0
# y=0
# res=0
# for n in range(n):
#     x= random.uniform(0,1)
#     y = random.uniform(0,1)
#     if (x*x+y*y) <=1:
#         res=res+1
# pi = 4*(res/n)   
# print(round(pi,n))



#ряд Нилаканта
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
    pi = 3.00
    num1 = 2
    num2 = 3
    num3 = 4
    n=1
    k= 1/10**(num_after_decimal_point+5)
    while k<n:
        n = 4 / (num1 * num2 * num3)
        num1 += 2
        num2 += 2
        num3 += 2
        n -= 4 / (num1 * num2 * num3)
        num1 += 2
        num2 += 2
        num3 += 2
        pi+=n
    return pi
n=input_int_in_range()
pi = get_pi(n)
print(3,14159265358979323846 )
print(pi)
print(round(pi,n))





