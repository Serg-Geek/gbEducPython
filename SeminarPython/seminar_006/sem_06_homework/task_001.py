# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
txt= input('input text-->>')
print(f"Исходный текст: {txt}")
find_abv = 'абв'
lst = [i for i in txt.split() if find_abv not in i]#list comprehension
print(f'result: {" ".join(lst)}')