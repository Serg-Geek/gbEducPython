# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def input_int():
    while True:
        try:
            n = int(input("Введите число: ")) 
            return n            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")   

n = input_int()
s = ''
while n>0:
    s = str(n %2 ) + s
    n = n // 2
print(s)