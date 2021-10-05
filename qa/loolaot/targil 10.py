num = int(input("number:"))
count=0
while num!=0:
    num = int(input("number:"))
    if (num%3==0) or (num%7==0):
        count+=1

print (count)