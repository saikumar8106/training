#WAP to check the type of triangle based on conditions
#where u take the input from the user for three sides and classify it accordingly
# into scalene isosceless equilateral

s1 = int(input('enter side 1 of triangle'))
s2 = int(input('enter side 2 of triangle'))
s3 = int(input('enter side 3 of triangle'))

if s1==s2 and s2==s3:
    print('equilateral triangle')
elif s1==s2 or s1==s3 or s2==s3:
    print('isosceless triangle')
else:
    print('scalene triangle')
