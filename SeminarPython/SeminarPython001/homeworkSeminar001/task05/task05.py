# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def input_float():
    while True:
        try:
            n = float(input("Введите число: ")) 
            return n            
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")    
          
print('Координата точки А по оси х')
ax = input_float()
print('Координата точки А по оси y')
ay = input_float()
print('Координата точки B по оси х')
bx = input_float()
print('Координата точки B по оси y')
by = input_float()
print()
print(f"Длина отрезка: {(((bx-ax)**2)+(by-ay)**2)**0.5}")
