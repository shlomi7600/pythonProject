def numcheck(lower,num1,upper):
    if lower<=num1<=upper:
        return True
    else:
        return False

lower=int(input("lower range:"))
num1=int(input("random number:"))
upper=int(input("upper range:"))

print (numcheck(lower,num1,upper))
if lower<=num1<=upper:
    print("nice")
else:
    print("nop")
