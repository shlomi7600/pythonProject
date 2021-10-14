from random import randint
number= randint(1,15)
guess=int(input("guess the number:"))

while number!=guess:
    if number>guess:
        print("the number is higher then yours,try again")
    else:
        print("the number is lower then yours ")
    guess = int(input("guess the number:"))
print("the number is equal")