x=int(input("Enter value: "))
x=str(x)
sum=0
for i in x:
    if int(i) % 2 !=0:
        sum+=int(i)
print(sum) 