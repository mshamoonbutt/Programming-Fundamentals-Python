#Ques No 1
def convert_temperature(temp, scale) :
    if scale=='F':
        print("Fahrenheit to Celsius")
        print((temp*9/5)+32)
    elif scale=='C':    
        print("Celsius to Fahrenheit") 
        print((temp-32)*5/9)
    else:
        print("invalid")
temp=eval(input("Enter your value of temperature: "))
scale=(input("F or C: "))
convert_temperature(temp, scale)        

#Ques No 2
def is_palindrome(string):
    cleaned_string = string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]

# Take a sentence from the user as input
user_input = input("Enter a sentence to check if it's a palindrome: ")

result = is_palindrome(user_input)

if result:
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')

#Ques No 3
# Get user input for section and the total number of tickets
section = input("Select a section (A, B, C): ")
total_num_tickets = int(input("Enter the total number of tickets: "))

# Define a function to calculate the ticket cost
def calculate_ticket_cost(section, total_num_tickets):
    # Define section prices
    section_prices = {'A': 50, 'B': 40, 'C': 30}
    
    # Calculate the total cost before any discounts
    total_cost = section_prices[section] * total_num_tickets
    discount = 0

    # Apply discounts
    if section == "B" and total_num_tickets >= 2:
        discount += 0.20 * total_cost
    elif total_num_tickets >= 5:
        discount += 0.10 * total_cost

    # Calculate the total cost after applying discounts
    total_discount = total_cost - discount

    # Print the results
    print(f"Number of tickets: {total_num_tickets}")
    print(f"Total cost before discount: {total_cost}")
    print(f"Total cost after discount: {total_discount}")

# Call the function with user inputs
calculate_ticket_cost(section, total_num_tickets)

#Ques No 4
def alarm_clock():
    # Get the current time and alarm time from the user as integers
    current_time = int(input("Enter the current time (in 24-hour format, e.g., 0830 for 8:30 AM): "))
    alarm_time = int(input("Enter the alarm time (in 24-hour format): "))

    # Check if the current time matches the alarm time
    if current_time == alarm_time:
        print("Time to wake up!")
    else:
        # Check if the current time is greater than the alarm time
        if current_time > alarm_time:
            print("You missed your alarm.")
        else:
            print("You still have time to sleep.")

# Run the alarm clock program
alarm_clock()


