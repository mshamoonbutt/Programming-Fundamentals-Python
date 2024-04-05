'''Write a program that reads a number between 1,000 and 999,999 from the user and
prints it with a comma separating the thousands.'''

x=int(input('Enter the number: '))
print('{:,}'.format(x))