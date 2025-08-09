
grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C"
}

while True:
    print("\n1. Add Student")
    print("2. Update Grade")
    print("3. View All Grades")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        grades[name] = grade
        print(f"{name} added with grade {grade}")
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in grades:
            grade = input("Enter new grade: ")
            grades[name] = grade
            print(f"{name}'s grade updated to {grade}")
        else:
            print("Student not found.")
    elif choice == "3":
        for student, grade in grades.items():
            print(f"{student}: {grade}")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")
