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