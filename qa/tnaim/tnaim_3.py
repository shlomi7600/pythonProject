from random import randint

age= randint(0,120)
print("random age:",age)

if 0<=age<=18:
    print("child")
if 19<=age<=60:
    print ("adult")
if 61<=age<=120:
    print("senior")
if 0>age or age>120:
    print("invalid age")