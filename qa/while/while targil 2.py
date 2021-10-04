age= int(input("age:"))

while 0>age or age>120:
    print("invalid age")
    age= int(input("age:"))
if 0 <= age <= 18:
    print("child")
if 19<=age<=60:
    print ("adult")
if 61<=age<=120:
    print("senior")


age= int(input("age:"))