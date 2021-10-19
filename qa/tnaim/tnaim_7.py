day=int(input("DD:"))
month=int(input("MM:"))
year=int(input ("YYYY:"))

if 1<=day<=31:
    print(day)
else:
    print("error")

if 1<=month<=12:
    print (month)
else:
    print('error')

if 1950<=year<=2021:
    print(year)
else:
    print("error")

if 2000<=year<=2009:
    print(f"{day}/{month}/{year%100}{year%100}")

if 1950<=year<=1999 or 2010<=year<=2021:
    print(f"{day}/{month}/{year%100}")