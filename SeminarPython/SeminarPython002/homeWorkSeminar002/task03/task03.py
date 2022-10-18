# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# *Пример:*

#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06


def input_int():
    while True:
        try:
            n = int(input("Введите число: ")) 
            return n            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")      

def get_list_subsequense(num):
    num_list=[]
    for i in range(1, num+1):
        res = (1+1/i)**i
        num_list.append(res)
    return (num_list)

def sum_list(list):
    sum = 0
    for i in range(0, len(list)):
        sum = sum+ list[i]
    return sum
n=input_int()
res= get_list_subsequense(n)
print()
print(res)
sum = sum_list(res)
print('sum subsequense for {n} =', sum)