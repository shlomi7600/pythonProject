word=input("say somthing:")
newword=''

for i in word:
    if word.count(i)>1 and i not in newword:
        newword+=i
print(newword)
