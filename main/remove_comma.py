'''Write a program that reads a number between 1,000 and 999,999 from the user,
where the user enters a comma in the input. Then print the number without a
comma. Here is a sample dialog; the user input is in color:
Please enter an integer between 10,000 and 99,999: 23,456
23456'''

x=input('Enter an integer between 10,000 and 99,999: ')
print(x.replace(',',''))