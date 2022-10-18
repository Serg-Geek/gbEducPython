# 5) Реализуйте алгоритм перемешивания списка.

import random
from re import L
def mixList(list=[]):
    l=len(list)
    for i in range(l-1,2,-1):
        j=random.randint(0, i-1)
        temp=list[i]
        list[i]= list[j]
        list[j] =  temp
    return list
list = input("Введите список чисел или символов, разделенных пробелом: ").split() 
print(list)
print()
print(mixList(list))
