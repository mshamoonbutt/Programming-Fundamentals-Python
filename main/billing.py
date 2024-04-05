def calculate_billing_amount(hourly_rate, consulting_time, low_income):
    """
    Calculate the billing amount for tax assistance.

    Args:
    hourly_rate (float): The hourly rate for tax assistance.
    consulting_time (int): The total consulting time in minutes.
    is_low_income (bool): True if the person has low income, False otherwise.

    Returns:
    float: The billing amount.
    """
    if low_income:
        if consulting_time <= 30:
            return 0.0  # No charges for low-income clients with <=30 minutes of consulting time
        else:
            time_over_30_minutes = consulting_time - 30
            service_charges = hourly_rate * 0.40 * (time_over_30_minutes / 60)
            return service_charges
    else:
        if consulting_time <= 20:
            return 0.0  # No service charges for others with <=20 minutes of consulting time
        else:
            time_over_20_minutes = consulting_time - 20
            service_charges = hourly_rate * 0.70 * (time_over_20_minutes / 60)
            return service_charges

# Prompt the user for input
hourly_rate = float(input("Enter the hourly rate for tax assistance: $"))
consulting_time = int(input("Enter the total consulting time in minutes: "))
low_income = input("Is the person low-income (yes/no)? ").strip().lower() == "yes"

# Calculate the billing amount
billing_amount = calculate_billing_amount(hourly_rate, consulting_time,low_income)

# Display the billing amount
print(f"Billing Amount: ${billing_amount:.2f}")