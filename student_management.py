import json
FILE_NAME = "students.json"

#======================================

# Load students from file

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
#=======================================
# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

#========================================
# Add a new student
def add_student(students):
    student_id = input("Enter Student ID: ")
#========================================

    # Check if ID already exists
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student added successfully.")

#========================================
# View all students
def view_students(students):
    if not students:
        print("No students found.")
        return

    print("\n===== STUDENT DETAILS =====")

    for student in students:
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Course     :", student["course"])
        print("---------------------------")

#=========================================
# Search student
def search_student(students):
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("Student ID :", student["id"])
            print("Name       :", student["name"])
            print("Age        :", student["age"])
            print("Course     :", student["course"])
            return

    print("Student not found.")

#============================================
# Update student
def update_student(students):
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:

            print("\nEnter new details:")

            student["name"] = input("Enter Name: ")
            student["age"] = input("Enter Age: ")
            student["course"] = input("Enter Course: ")

            save_students(students)

            print("Student updated successfully.")
            return

    print("Student not found.")

#===========================================
# Delete student
def delete_student(students):
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:

            students.remove(student)
            save_students(students)

            print("Student deleted successfully.")
            return

    print("Student not found.")

#=================================================
# Main program
def main():

    students = load_students()

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

#================================================
# Run the program
if __name__ == "__main__":
    main()