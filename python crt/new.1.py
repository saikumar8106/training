#WAP to check whether the year is leap year or not with conditions
# if the year is divisible by 4 and not by 100 or if it is divisible by 400then the year is
# leap year

year = int(input('enter an year'))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,"is a leap year")
else:
    print(year,'is not a leap year')
