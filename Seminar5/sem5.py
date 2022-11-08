#  В файле находится N натуральных чисел, записанных через пробел. 
# # # Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

with open('/home/user/Python/gbEducPython/Seminar5/text.txt', 'r') as data:
    lst= data.readline()
print(lst)
lst = [int(x) for x in  lst.split()]

l = [x for x in range(1, len(lst)) if lst[x-1]!=(lst[x]-1)]
print(l)

etalon_list = [x for x in range (len(lst)+1)]
print(etalon_list)
num=0
for i in range(len(lst)):
    if i == len(lst):
        num = lst[i]+1
    if lst[i] == etalon_list[i]:
        continue
    else:
        num = lst[i]-1
        break
print(num)



l = [x for x in range(1, len(lst)) if lst[x-1]!=(lst[x]-1)]
print(l)



a = list(filter(lambda x : x[0]-1 == lst[x[1]-1] if x[1] > 0 else True, list(zip(lst,range(len(lst))))))

print(list(zip(lst,range(len(lst)))))

# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.
    
#     *Пример:* 
    
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# l= [1,5,2,3,4,6,1,7]
# n=[]
# while                   
# 
# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв
# 
# # 
# a = ['абв Ура, питон крутой абвязык , очень интересные семинарабвы ДЗ! абв']
# c= 'абв'
# b = [a - filter(c, a)]
# print(b)

    

