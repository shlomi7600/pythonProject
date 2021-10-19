# import random
# list1 = []
# for i in range(20):
#     randomnum = random.randint(1,100)
#     list1.append(randomnum)
# # if randomnum==mynum:
# # list1.remove(randomnum)
#
# print(list1)
#
# mynum=int(input("choose a number between 1-100:"))
#
# for i in list1:
#     if  randomnum==mynum:
#         list1.remove(randomnum)

from random import randint
list1=[randint (1,100) for i in range (20)]
print (list1)
num=int(input("enter number to remove:"))

while num in list1:
    list1.remove(num)

print(list1)