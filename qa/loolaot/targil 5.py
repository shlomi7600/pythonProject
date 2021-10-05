count=0
sum1=0

score = int(input("score:"))
while 100>score>0:
    if 0 < score < 100 and score > 60:
         score = int(input("score:"))
         sum1+=score
         count+=1
    if 0<score<100 and score<60:
         score = int(input("score:"))
    if 0>score or 100<score:
        print("invalid score")
        break

if count>1:
    print(f"the avarege score of the pass class is:{(sum1/count)}")
