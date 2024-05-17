def find_highest_quantity_item(inventory):
    if len(inventory) == 0:
        return None

    highest_quantity = -1
    highest_quantity_item = None

    for item, quantity in inventory.items():
        if quantity > highest_quantity:
            highest_quantity = quantity
            highest_quantity_item = item

    return highest_quantity_item

sample_inventory = {'item1': 10, 'item2': 5, 'item3': 8, 'item4': 12, 'item5': 6}

highest_quantity_item = find_highest_quantity_item(sample_inventory)

if highest_quantity_item is not None:
    print(f"The item with the highest quantity is: {highest_quantity_item}")
else:
    print("Inventory is empty.")