# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1
st= input("input num-->>") 
lst=list(st)
print("последовательность цифр-->>",st)
dct={}
lst=list(filter(str.isdigit, lst))# фильтр убирает символы и оставляет в списке только цифры1122
int_lst = [int(x) for x in lst]#list comprehension
analysis(int_lst, dct)
dct=dict(filter(lambda item: item[1]==1, dct.items()))# filter удаляет нессоответствующие кортежи из словаря
print('список неповторяющихся элементов -->>', list(dct.keys()))
