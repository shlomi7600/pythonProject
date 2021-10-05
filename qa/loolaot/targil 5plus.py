count=0
count2=0
sum1=0
sum2=0
for i in range (5):
    score = int(input("score:"))
    if 0<score<100 and score>60:
        sum1+=score
        count+=1
    if 0<score<100 and score<60:
        sum2+=score
        count2+=1
    if 0>score or 100<score:
        print("invalid score")

if count>1:
    print(f"the avarege score of the pass class is:{(sum1/count)}")
    print(f"the avarege score of the failed class is:{(sum2 / count2)}")