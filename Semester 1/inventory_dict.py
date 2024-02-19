# Create a dictionary representing inventory items
inventory = {'item1': 10, 'item2': 5, 'item3': 20, 'item4': 15}

# Write a function to find the item with the highest quantity
def highest_quantity_item(inventory_dict):
    max_quantity = max(inventory_dict.values())
    for item, quantity in inventory_dict.items():
        if quantity == max_quantity:
            return item

# Call the function and print the result
result_item = highest_quantity_item(inventory)
print(f"The item with the highest quantity is: {result_item}")