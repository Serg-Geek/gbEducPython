# s = "abcdefghijklmnop"
# while s != "":
#     print (s)
#     s = s[1:-1] 

# for i in range(1, 10):
#      for j in range(1, 10):
#             print ("%2i" % (i*j))
#      print()    

from datetime import datetime
import random
from time import sleep
import time

# odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
#  21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
#  41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]
# right_this_minute = datetime.today().minute
# for i in range(5):
#     if i<5:
        
#         if right_this_minute in odds:
#             print("This minute seems a little odd.")
#         else:
#             print("Not an odd minute.")
#         time.sleep(random.randint(1,60))

# print(datetime.today().minute, datetime.today().second,  datetime.today().microsecond, datetime.today())

word = "bottles" 
for beer_num in range(99, 0, -1): 
    print(beer_num, word, "of beer on the wall.") 
    print(beer_num, word, "of beer.") 
    print("Take one down.") 
    print("Pass it around.") 
    time.sleep(4)
    if beer_num == 1: 
        print("No more bottles of beer on the wall.") 
    else: 
        new_num = beer_num - 1 
        if new_num == 1: 
                word = "bottle" 
        print(new_num, word, "of beer on the wall.") 
    print()

