word=input("say something: ")
#newword=word.replace('A','')
#newword=word.replace('a','')
#print (newword)

newword1=''
for i in word:
    if i!='A' and i!='a':
        newword1+=i
print (newword1)
