'''Write a program that helps a person decide whether to buy a hybrid car. Your
program’s inputs should be:
• The cost of a new car
• The estimated miles driven per year
• The estimated gas price
• The efficiency in miles per gallon
• The estimated resale value after 5 years
Compute the total cost of owning the car for
five years. (For simplicity, we will not take the
cost of financing into account.) Obtain
realistic prices for a new and used hybrid
and a comparable car from the Web. Run your program twice, using today’s gas
price and 15,000 miles per year. Include pseudocode and the program runs with your
assignment.'''

cost=int(input('Enter Price Of Car: '))
miles=int(input('Enter miles car driven per year: '))
gas=int(input('Enter price of gas: '))
efficiency=int(input('Enter efficiency in miles per gallon: '))
resale=int(input('Enter estimated resale value after 5 years: '))
total_cost=(cost+(gas*(miles/efficiency)))-resale
print(f"The total cost of owning the car for five years is {total_cost}")