word= input("enter word:")
character=input("enter character:")

count=0

for i in word:
    if character==i:
        count+=1

print(count)