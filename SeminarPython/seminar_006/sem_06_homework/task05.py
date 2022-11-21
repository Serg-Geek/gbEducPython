# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0


def get_parts(txt):
    l = lambda a: a if a!='-' else '+-'
    txt2="".join([l(x) for x in list((txt.split("=").pop(0))) if x!=' ']).split('+')
    txt2.pop(0)
    l = lambda a: ('^0',a[0]) if len(a)==1  else (a[1],a[0])if len(a[1])>0 else ('^1', a[0])
    txt2=[l(x.split('x')) for x in txt2]
    return txt2
def sum_parts(l_1,l_2):
    l=lambda a : int(a[0].replace('^',''))
    m = lambda a : int(a[1])
    res=[]
    el_1=el_2=0
    while len(l_1)>0 or len(l_2)>0:
        if not el_1:
            if len(l_1)>0: el_1=l_1.pop(0) 
            else :el_1= ('^0','0') 
        if not el_2:
            if len(l_2)>0: el_2=l_2.pop(0) 
            else :el_2= ('^0','0') 
        if l(el_1) >l(el_2):
            res.append((m(el_1),el_1[0])) 
            el_1 = 0
        elif l(el_1) < l(el_2):
            res.append((m(el_2),el_2[0]))
            el_2 = 0
        else: 
            res.append(( m(el_1)+ m(el_2),el_1[0]))
            el_1 = el_2 = 0
    return res
with open('/home/user/Python/gbEducPython/SeminarPython/seminar_006/sem_06_homework//task005.txt', 'r') as data:
    lst= data.readline()
with open('/home/user/Python/gbEducPython/SeminarPython/seminar_006/sem_06_homework//task04.txt', 'r') as data:
    lst_1= data.readline()     
parts_1 = get_parts(lst)
parts_2 = get_parts(lst_1)
list_sum =sum_parts(parts_1,parts_2)
result =(' + '.join(map(lambda i:str(i[0])+'x'+i[1], list_sum))).replace('+ -','- ') +' = 0'
result = result.replace('^1','').replace('x^0','')
print(result,'(результат также записан в файл "result.txt")')
with open ('/home/user/Python/gbEducPython/SeminarPython/seminar_006/sem_06_homework/result.txt', 'w') as file:
    file.write(result)






