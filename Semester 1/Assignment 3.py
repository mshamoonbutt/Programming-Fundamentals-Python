#Ques No 1
def multiset_union(set1, set2):
    """
    Compute the union of two multisets represented as dictionaries.

    Args:
    set1 (dict): The first multiset represented as a dictionary.
    set2 (dict): The second multiset represented as a dictionary.

    Returns:
    dict: The dictionary representing the union of the multisets.
    """
    union_dict = set1.copy()

    for key, value in set2.items():
        if key in union_dict:
            union_dict[key] += value
        else:
            union_dict[key] = value

    return union_dict

def multiset_intersection(set1, set2):
    """
    Compute the intersection of two multisets represented as dictionaries.

    Args:
    set1 (dict): The first multiset represented as a dictionary.
    set2 (dict): The second multiset represented as a dictionary.

    Returns:
    dict: The dictionary representing the intersection of the multisets.
    """
    intersection_dict = {}

    for key, value in set1.items():
        if key in set2:
            intersection_dict[key] = min(value, set2[key])

    return intersection_dict

def multiset_difference(set1, set2):
    """
    Compute the difference of two multisets represented as dictionaries.

    Args:
    set1 (dict): The first multiset represented as a dictionary.
    set2 (dict): The second multiset represented as a dictionary.

    Returns:
    dict: The dictionary representing the difference of the multisets.
    """
    difference_dict = set1.copy()

    for key, value in set2.items():
        if key in difference_dict:
            difference_dict[key] = max(difference_dict[key] - value, 0)
        else:
            difference_dict[key] = 0

    return difference_dict

# Example usage:
set1 = {'apple': 2, 'banana': 3, 'orange': 1}
set2 = {'banana': 2, 'grapes': 4, 'orange': 1}

union_result = multiset_union(set1, set2)
intersection_result = multiset_intersection(set1, set2)
difference_result = multiset_difference(set1, set2)

print("Union:", union_result)
print("Intersection:", intersection_result)
print("Difference:", difference_result)




#Ques No 2
def sparseArraySum(a, b):
    """
    Compute the vector sum of two sparse arrays represented as dictionaries.

    Args:
    a (dict): The first sparse array represented as a dictionary.
    b (dict): The second sparse array represented as a dictionary.

    Returns:
    dict: The dictionary representing the vector sum of the sparse arrays.
    """
    result = {}

    for key in set(a.keys()).union(b.keys()):
        result[key] = a.get(key, 0) + b.get(key, 0)

    return result

# Example usage:
sparse_array_a = {5: 4, 9: 2, 10: 9}
sparse_array_b = {2: 3, 5: 1, 9: 5}

result_sum = sparseArraySum(sparse_array_a, sparse_array_b)
print("Vector Sum:", result_sum)


#Ques No 3
def invert_dict(input_dict):
    """
    Invert the keys and values of a dictionary. Handles cases where multiple keys have the same value.

    Args:
    input_dict (dict): The input dictionary.

    Returns:
    dict: The inverted dictionary.
    """
    inverted_dict = {}

    for key, value in input_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]

    return inverted_dict

# Example usage:
original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
inverted_result = invert_dict(original_dict)

print("Original Dictionary:", original_dict)
print("Inverted Dictionary:", inverted_result)



#Ques No 4
def discount(prices, isPet, nItems):
    pet_count = sum(isPet)
    other_items_count = nItems - pet_count

    if pet_count >= 1 and other_items_count >= 5:
        other_items_total = sum(prices[i] for i in range(nItems) if not isPet[i])
        discount_amount = 0.2 * other_items_total
        return discount_amount
    else:
        return 0

if __name__ == "__main__":
    prices = []
    isPet = []
    nItems = 0

    while True:
        price = float(input("Enter price (-1 to stop): "))
        if price == -1:
            break

        pet = input("Is it a pet? (Y/N): ").upper() == 'Y'

        prices.append(price)
        isPet.append(pet)
        nItems += 1

    discount_amount = discount(prices, isPet, nItems)
    print(f"Discount Amount: ${discount_amount:.2f}")



#Ques No 5

def read_file(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            key = parts[0].strip()
            values = [v.strip() for v in parts[1:]]  # Trim whitespaces
            data[key] = values
    return data

def query_information():
    # Read data from three files
    names_and_numbers = read_file('names_and_numbers.csv')
    names_and_ssns = read_file('names_and_ssns.csv')
    ssns_and_incomes = read_file('ssns_and_incomes.csv')

    # Ask the user for a telephone number
    telephone_number = input("Enter a telephone number: ").strip()

    # Check if the telephone number is present in values of names_and_numbers
    for key, values in names_and_numbers.items():
        if telephone_number in values:
            name = key

            # Check if the name is present in names_and_ssns
            if name in names_and_ssns:
                ssn = names_and_ssns[name][0]

                # Check if the ssn is present in ssns_and_incomes
                if ssn in ssns_and_incomes:
                    income = ssns_and_incomes[ssn][0]

                    # Print the information
                    print(f"Details for {telephone_number}:\n"
                          f"Name: {name}\nSSN: {ssn}\nIncome: {income}")
                    return  # Exit the function once information is found

    # If the loop completes without finding information
    print("Details not found for the given telephone number.")

if __name__ == "__main__":
    query_information()



#Ques No 6

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
