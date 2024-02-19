# Create a nested dictionary to store information about students
students_dict = {
    'ID1': {'name': 'Student1', 'courses': ['Math', 'Science'], 'grades': {'Math': 90, 'Science': 85}},
    'ID2': {'name': 'Student2', 'courses': ['English', 'History'], 'grades': {'English': 92, 'History': 88}}
}

# Write a function to calculate the average grade for a student
def average_grade(student_dict, student_id):
    if student_id in student_dict:
        grades = student_dict[student_id]['grades'].values()
        avg_grade = sum(grades) / len(grades)
        return avg_grade
    else:
        return "Student ID not found."

# Call the function for a specific student and print the result
student_id_to_check = 'ID1'
average_grade_result = average_grade(students_dict, student_id_to_check)
print(f"The average grade for {students_dict[student_id_to_check]['name']} is: {average_grade_result}")