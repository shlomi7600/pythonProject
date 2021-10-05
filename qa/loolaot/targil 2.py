sum1=0
count=0
for i in range (6):
    number = (int(input("give me an number:")))
    if number%2==0:
        sum1+=number
        count+=1
print(f"sum of the numbers is:{sum1};the avarege is {sum1/count}")