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