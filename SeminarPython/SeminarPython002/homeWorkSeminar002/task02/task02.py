# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.  

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def input_int():
    while True:
        try:
            n = int(input("Введите число: ")) 
            return n            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    

num=input_int()
num_list=[]
for i in range(1, num+1):
    num_list.append(i)
   
print(num_list) 

def list_multiplicftion(x):
    result =[]
    p=1
    for i in x:
        p=p*i
        result.append(p)
    return(result)

pri=list_multiplicftion(num_list)
print(pri)

