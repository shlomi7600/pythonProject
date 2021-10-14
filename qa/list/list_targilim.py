list1=[]
for i in range (5):
    num=int(input("enter number:"))
    list1.append(num)

print(list1)
print("max",max(list1))
print("mim",min(list1))
print("average",sum(list1)/len(list1))