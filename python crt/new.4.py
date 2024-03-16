print first 10 fibanocci series
f1=0
f2=1
print(f1)
print(f2)
for i in range(3,11):
    sum = f1+f2
    print(sum)
    f1=f2
    f2=sum
