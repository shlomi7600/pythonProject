from random import randint
list1=[randint (1,100) for i in range (10)]
print (list1)
t1=()
t1=tuple(list1)
print(t1)
newnum=int(input("add new number:"))
t1+=(newnum,)
print(t1)

t2=t1[0:4]
t2+=t1[-4:]
print(t2)

