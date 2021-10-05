highscore=0
score = int(input("what's the score?"))
sum1=0
count=0
while 0<=score<=100:
    sum1+=score
    count+=1
    if highscore<score:
        highscore=score
    score = int(input("what's the score?"))

if count>0:
    print(highscore)
    print(sum1/count)
    print(highscore-(sum1/count))