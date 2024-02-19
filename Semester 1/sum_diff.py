'''Write a program that prompts the user for two integers and then prints
• The sum
• The difference
• The product
• The average
• The distance (absolute value of the difference)
• The maximum (the larger of the two)
• The minimum (the smaller of the two)
Hint: Python defines max and min functions that accept a sequence of values, each
separated with a comma.'''

x=int(input("Enter first value: "))
y=int(input("Enter second value: "))
sum=x+y
diff=x-y
pr=x*y
av=(x+y)/2
dis=abs(diff)
max=max(x,y)
min=min(x,y)
print(f"Sum:{sum}\nDifference:{diff}\nProduct:{pr}\nAverage:{av}\nDistance:{dis}\nMaximum:{max}\nMinimum:{min}")