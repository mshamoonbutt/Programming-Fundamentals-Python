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