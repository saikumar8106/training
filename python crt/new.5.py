print the given number is a prime or not without using count 
num = int(input('enter the number'))
flag = 0
for i in range(2,num):
    if num%i==0:
        flag = 1
        break
if flag==1:
    print("not a prime")
else:
    print("prime")
