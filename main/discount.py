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