list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
print(list1[-3::])
print(list1[::-1])
print(list1[1::2])
print(list1[:5])
print(list1[0::2])

number=int(input("new number:"))
list1[7:10]=[number]
print(list1)

list2=[]
for i in list1:
    if i%3==0:
     list1.remove(i)
    list2.append(i)
print (list1)
print(list2)

list2=[1,1]
for i in list2:
    if i*2<50:
        list2.append(i*2)
print (list2)

