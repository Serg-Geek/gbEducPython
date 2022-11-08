from unittest import result


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def input_int():
    while True:
        try:
            n = int(input("Введите число: ")) 
            return n            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.") 

def simple_mult(n):
    result = []
    n = int(n)
    x=2
    x=int(x)
    while x**2 <= n:
       if n %x ==0:
            result.append(x)
            n //=x
       else:
            x+=1
    if n>1:
        result.append(n)
    return result



print(simple_mult(input()))