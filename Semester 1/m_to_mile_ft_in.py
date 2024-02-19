#Write a program that prompts the user for a measurement in meters and then converts it to miles, feet, and inches.
x=int(input('Enter measurement in meters: '))
miles=x/1609
feet=x*3.281
inches=x*39.37
print(f"{x} meters = {miles} miles\n{x} meters = {feet} feet\n{x} meters = {inches} inches")