n=int(input("Enter the number: "))
while n!=-1:
    n=int(input("Enter the number: "))    
    if n>0:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
            print(f"Factorial of {n} is {fact}")
    elif n==-1:
        print("Exiting")
    elif n<-1:
        print("Invalid Input")
    else:
        print("Invalid Input")                