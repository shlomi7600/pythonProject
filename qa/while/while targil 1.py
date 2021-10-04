number=int(input("number beween 100-999:"))

while 100>number or number>999:
    print("error")
    number=int(input("number beween 100-999:"))

print((number%10)+(number//10%10)+(number//100))
