

def posl(x):
    return (x+1) // 2


n, x = map(int, input('enter integer number of elements and first number:').split())
sequence = [x]
for i in range(1, n+1):
    x = posl(x)
    sequence.append(x)
    print(x, end=' ')



def posl(x):
    return (x+1) // 2


n, x = map(int, input('enter integer number of elements and first number:').split())
sequence = [x]
for i in range(1, n+1):
    x = posl(x)
    sequence.append(x)
    print(x, end=' ')
От Sergey Ryabinin всем 09:50 PM
print(dct)    

#     3. Напишите программу, в которой пользователь будет задавать две строки, а программа - 
#           определять количество вхождений одной строки в другой.

text = input('enter text: ')
srch = input('enter substring to search: ')
lst = text.split(srch)
print(f'в строке {text} подстрока {srch} содержится {len(lst)-1} раз')



roman = [
['I', 1],
['II', 2],
['III', 3],
['IV', 4],
['V', 5],
['VI', 6],
['VII', 7],
['VIII', 8],
['IX', 9],
['X', 10],
['XX', 20],
['XXX', 30],
['XL', 40],
['L', 50],
['LX', 60],
['LXX', 70],
['LXXX', 80],
['XC', 90],
['C', 100],
['CC', 200],
['CCC', 300],
['CD', 400],
['D', 500],
['DC', 600],
['DCC', 700],
['DCCC', 800],
['CM', 900],
['M', 1000]
]
num = 910
conv =''
for i in range(len(roman)-1, -1, -1):
    if num // roman[i][1] > 0:
        conv = conv + roman[i][0]*(num // roman[i][1])
        num = num % roman[i][1]
print(conv)


text1 = input ('Введите текст:')
text2 = input ('Введите второй текст:')
len_find_text = len(text1)
count = 0
for i in range (len(text2)):
    if text2[i: i+len_find_text] == text1:
        count += 1
print (count)


number = int(input('Введите число: '))

binar_number = bin(number)
print(binar_number)

print(binar_number.count('1'))
