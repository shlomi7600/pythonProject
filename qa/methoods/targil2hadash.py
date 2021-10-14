def numchecker(num1):
    if 100<=num1<=999:
        return True
    else:
        return False

num1=int(input("give me a number:"))
if numchecker(num1):
    print("the number is in range")
else:
    print("the number isn't in the range")