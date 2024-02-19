#Ques No 1

def generate_cubes_dict():
    cubes_dict = {}
    for num in range(1, 6):
        cubes_dict[num] = num ** 3
    return cubes_dict

cubes_dict = generate_cubes_dict()

print(cubes_dict)


#Ques No 2

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
    
    
#Ques No 3


def calculate_average_grade(student_info, student_id):
    if student_id not in student_info:
        return f"Student with ID {student_id} not found."

    grades = student_info[student_id]["grades"]

    if len(grades) == 0:
        return f"No grades available for student with ID {student_id}."
    
    average_grade = sum(grades.values()) / len(grades)
    return f"The average grade for student with ID {student_id} is: {average_grade:.2f}"

students_info = {
    1: {
        "name": "John",
        "courses": ["Math", "Physics", "History"],
        "grades": {"Math": 85, "Physics": 90, "History": 75}
    },
    2: {
        "name": "Alice",
        "courses": ["English", "Chemistry", "Biology"],
        "grades": {"English": 92, "Chemistry": 88, "Biology": 95}
    }
}

student_id_to_check = 1
result = calculate_average_grade(students_info, student_id_to_check)

print(result)
  



