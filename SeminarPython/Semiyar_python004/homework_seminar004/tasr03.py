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
int_lst = [int(x) for x in lst]
analysis(int_lst, dct)
res=[]
for k, v in dct.items():
        if v == 1:
           res.append(k)
print('список неповторяющихся элементов -->>',res)

