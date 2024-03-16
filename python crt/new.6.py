#calculate the sum of digits of a number which is taken as input from the user
n = int(input('enter a number'))
r = 0
sum = 0
q = 0
while n!=0:
    q = n//10
    r = n%10
    sum = sum+r
    n = q
print(sum)
