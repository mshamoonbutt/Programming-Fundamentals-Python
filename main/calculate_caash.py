def calculate_cash(file_path, start_cash):
    # Initialize cash variables
    current_cash = start_cash

    # Read transactions from the file
    with open(file_path, 'r') as file:
        for line in file:
            invoice, amount, transaction_type = line.split()
            amount = float(amount)

            # Update cash based on transaction type
            if transaction_type == 'P':
                current_cash += amount
            elif transaction_type == 'R':
                current_cash -= amount

    return current_cash

if __name__ == "__main__":
    # Get user input
    start_cash = float(input("Enter the amount of cash at the beginning of the day: "))
    end_cash = float(input("Enter the expected amount of cash at the end of the day: "))
    file_path = input("Enter the name of the file with transactions: ")

    # Calculate actual amount of cash at the end of the day
    actual_end_cash = calculate_cash(file_path, start_cash)

    # Check if the actual amount matches the expected amount
    if actual_end_cash == end_cash:
        print("The actual amount of cash matches the expected amount.")
    else:
        print("The actual amount of cash does not match the expected amount.")