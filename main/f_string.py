#Ques No 1
name=str(input("Name: "))
age=int(input("Age: "))
favorite_colour=str(input("Favorite Colour: "))
output=f"Hello, my name is {name}. I am {age} years old, and my favorite colour is {favorite_colour}."
print(output)

#Ques No 2
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))
c = int(input("Enter the third integer (c): "))
result = (a * b) + (c ** 2) - 5
output = f"({a} * {b}) + ({c} ** 2) - 5 = {result}"
print(output)

#Ques No 3
length=float(input("Enter Length of Rectangle: "))
width=float(input("Enter width of Rectangle: "))
area = length * width
output = f"The area of the rectangle is {area} square units."
print(output)

#Ques No 4
Item_1=input("Enter first product: ")
Item_2=input("Enter second product: ")
Item_3=input("Enter third product: ")
print("Item         Weight         Cost")
output1 = f"{Item_1}           2            1000"
output2 = f"{Item_2}          3            220"
output3= f"{Item_3}          4            300"
print(output1)
print(output2)
print(output3)

print("---------------------------------")
print("Total                       1520")