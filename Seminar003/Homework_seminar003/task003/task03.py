# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def input_float():
    while True:
        try:
            n = float(input("--->  ")) 
            return n            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.") 

def input_int():
    while True:
        try:
            n = int(input("---> ")) 
            return n            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.") 
print('Введите длину списка')
len_list=input_int()
float_list= []
dec_fraction=[]

for i in range(0, len_list):
    print('вещестренное число')
    float_list.append(input_float())

for i in range(0, len(float_list)):
    dec_fraction.append(float_list[i]%1)
print(dec_fraction)
print('разницa между максимальным и минимальным значением дробной части элементов')
print(max(dec_fraction)-min(dec_fraction))

# второй способ
for i in range(0, len(float_list)):
    dec_fraction.append (float_list[i]- int (float_list[i]))
print(max(dec_fraction)-min(dec_fraction))
