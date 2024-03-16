#reverse of a number as digits using while loop:
rem = 0
q = 0
count = 0 
n = int(input('enter a number to reverse the digits: '))
while(n!=0):
    rem = n%10
    q = n//10
    count = count + 1
    n = n//10
    print(rem)
