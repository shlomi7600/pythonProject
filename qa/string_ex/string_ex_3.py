word1=input("write somthing:")
word2=input("write somthing:")

if word2 in word1:
    for i in range(len(word1)):
        if word1[i]==word2:
            print (i)
            break
else:
    print("-1")