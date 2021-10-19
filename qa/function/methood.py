def avarege(num1,num2):
    avg=(num1+num2)/2
    return  avg

def valid_grade (grade):
    if 0<=grade<=100:
        return True
    else:
        return False

grade1=int(input("enter grade 1:"))
grade2=int(input("enter grade 2:"))

print(avarege(grade1,grade2))

if valid_grade(grade1):
    print("grade1 is valid")

else:
    print("grade1 is invalid")

if valid_grade(grade2):
    print("grade1 is valid")

else:
    print("grade1 is invalid")