def leap_year(year):
    """
    Check if a year is a leap year.

    Args:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        return True
    return False

def days_in_month_calculation(m, year):
    """
    Calculate the number of days in a specific month.

    Args:
    m (int): The month (1-12) to calculate the days for.
    year (int): The year for potential leap year calculation.

    Returns:
    int: The number of days in the specified month.
    """
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    elif m == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30

# Input date, month, and year
month = int(input("Enter month (1-12): "))
date = int(input("Enter date (1-31): "))
year = int(input("Enter year (0-2023): "))

m = 1
days_in_month = 0
while m <= month:
    if m == month:
        days_in_month += date
    else:
        days_in_month += days_in_month_calculation(m, year)
    m += 1

# Printing number of days
output_days = days_in_month
print(f"The day number of {month}-{date}-{year} is {output_days}")