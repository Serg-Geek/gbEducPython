# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

# from turtle import numinput


# def is_sqr(x,y):
#     return x**2==y or y**2==x

# a=int(input())
# b=int(input())
# if is_sqr(a,b):
#     print('yes')
# else:
#     print('no')


#     2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# def find_max(a,b,c,d,g):
#     max=a
#     if max<b:
#         max=b
#     if max<c:
#         max=c
#     if max<d:
#         max=d
#     if max<g:
#         max=g
#     return max

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# g=int(input())
# max=find_max(a,b,c,d,g)
# print(max)


# nums =[0,0,0,0,0]
# nums[0]=int(input())
# nums[1]=int(input())
# nums[2]=int(input())
# nums[3]=int(input())
# nums[4]=int(input())
# max = nums[0]
# for i in nums:
    
#     if i >max:
#       max = i
# print(max)


nums = input("Введите список чисел, разделенных пробелом: ").split()
print("Список: ", nums)
max_num = int(nums[0])
for i in range(len(nums)):
    if max_num < int(nums[i]):
        max_num= int(nums[i])
print(max_num)

