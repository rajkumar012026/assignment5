student_marks = {
    "Rajkumar Sah": 89.90,
    "Amar Kumar": 90.25,
    "Madan Kumar": 85.10
}
while True:
    student_name = input("Please enter the name of the student: ")
    if student_marks.get(student_name) == None:
        print("Student not found")
        continue
    else:
        print(f"{student_name}'s marks :", student_marks.get(student_name))
        break