word1= input("say somthing: ")
word2= input("say somthing: ")
list1=[]

for i in word1:
    if word1.count(i) and word2.count(i) and i not in list1:
        list1.append(i)

print(list1)