def table(x):
    for i in range(1,11):
        product=x*i
        print(f"{x} x {i} = {product}")       
x=int(input("Enter value of x: "))
 
table(x)