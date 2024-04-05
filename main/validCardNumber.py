def card_check(card_number):
    """
    Check if a credit card number is valid and provide intermediate steps.

    Args:
    card_number (str): A string representing an 8-digit credit card number.

    Returns:
    str: A message indicating if the number is a valid card number or not.
    """

    # Step 1: Calculate the sum (A) of every other digit starting from the rightmost digit
    sum_a = 0
    for i in range(7, -1, -2):
        digit = int(card_number[i])
        sum_a += digit

    print(f"A: {sum_a}")

    # Step 2: Calculate the digit-sequence formed by doubling and adding all digits not included in A
    sum_b = 0
    sequence = ""
    for i in range(6, -1, -2):
        digit = int(card_number[i])
        doubled_digit = digit * 2
        sequence += str(doubled_digit)

        if doubled_digit >= 10:
            sum_b += doubled_digit // 10 + doubled_digit % 10
        else:
            sum_b += doubled_digit

    print(f"Sequence: {sequence}")
    print(f"B: {sum_b}")

    # Step 3: Calculate the total sum (A + B)
    total_sum = sum_a + sum_b
    print(f"A+B: {total_sum}")

    # Check if the total sum's last digit is 0
    if total_sum % 10 == 0:
        return "Valid card number"
    else:
        valid_digit = (10 - (total_sum % 10)) % 10
        return f"Invalid card number. The last digit to make it valid is: {valid_digit}"

# Get user input and call the function
card_number = input("Please input the credit card number (8 digits): ")
result = card_check(card_number)
print(result)
