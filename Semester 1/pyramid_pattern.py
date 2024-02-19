def pattern(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print("*", end='')
        print("") 
x=int(input("Enter x: "))          
pattern(x)            

def pattern(rows):
    for i in range(rows, 0, -1):
        print('*' * i)

rows = int(input("Enter the number of rows: "))
pattern(rows)

def pattern(x):
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()

x = int(input("Enter x: "))
pattern(x)

def pattern(x):
    for i in range(x, 0, -1):
        for j in range(1,i+1):  
            print(j,end='')
        print()

x = int(input("Enter x: "))
pattern(x)