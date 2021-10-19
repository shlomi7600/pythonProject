def sum_digit (num):
        sumdigits=((num//100)+(num//10%10)+(num%10))
        return  sumdigits

randomnum=int(input("random number between 100-999:"))
print(sum_digit(randomnum))

