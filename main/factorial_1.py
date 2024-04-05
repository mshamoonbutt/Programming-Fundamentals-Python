def factorial(x):
    result=1
    for i in range(1,x+1):
        result*=i
    print(result)    
    
x=int(input("Enter value of x: "))
factorial(x) 