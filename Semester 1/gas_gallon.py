'''Write a program that asks the user to input
• The number of gallons of gas in the tank
• The fuel efficiency in miles per gallon
• The price of gas per gallon
Then print the cost per 100 miles and how far the car can go with the gas in the tank.'''

gallon=float(input('Enter number of gallons of gas in the tank: '))
efficiency=float(input('Enter fuel efficiency in miles per gallon: '))
price=float(input('Enter price of gas per gallon: '))
cost_per_100_mile=(100/efficiency)+price
travel_distance=gallon/efficiency
print(f"Cost of fuel per 100 miles is {cost_per_100_mile:.2f}")
print(f"Car can go {travel_distance:.2f} miles with current {gallon:.2f} gallon present in the tank.")