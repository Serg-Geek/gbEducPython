# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def input_int():
    while True:
        try:
            n = int(input("Введите число: ")) 
            return n            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.") 

def Fibonacci(n):
    f =1
    if n>1:
        f = Fibonacci(n-1) + Fibonacci(n-2)
    return f
def nega_Fibonacci(n):
    f =1
    if n<1:
        f = nega_Fibonacci(n+2) - nega_Fibonacci(n+1)
    return f
n=input_int()
nega_fib_list =[]
for i in range(0,(-n-1),-1):
    nega_fib_list.append(nega_Fibonacci(i))
nega_fib_list.reverse()
result_fib_list=nega_fib_list
for i in range(n):
    result_fib_list.append(Fibonacci(i))
print(result_fib_list)

