# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

def input_float():
    while True:
        try:
            n = float(input("Введите число: ")) 
            return n            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    

num = input_float()
numstr =str(num)
sum=0
for i in numstr:
    if i!='.':
        sum = sum +int (i)
print('вы ввели число; ', numstr)
print('cумма цифр в числе = ', sum)

# второй вариант

a=num
b=str(a)
sum1=0
for x in range(9):
    sum1=sum1 + x*b.count(str(x))
print('cумма цифр в числе = ', sum1 )
