import json

FILE_NAME = "students.json"
# ==========================================
# Load students from JSON file
# ==========================================
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: Invalid data in students.json")
        return []
# ==========================================
# Save students to JSON file
# ==========================================
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)
# ==========================================
# Get valid age
# ==========================================
def get_valid_age():
    while True:

        age = input("Enter Age: ")

        if age.isdigit():

            age = int(age)

            if 1 <= age <= 100:
                return age

            print("Age must be between 1 and 100.")

        else:
            print("Please enter a valid number.")
# ==========================================
# Get valid phone number
# ==========================================
def get_valid_phone():

    while True:

        phone = input("Enter Phone Number: ")

        if phone.isdigit() and len(phone) == 10:
            return phone

        print("Please enter a valid 10-digit phone number.")
# ==========================================
# Get valid email
# ==========================================
def get_valid_email():

    while True:

        email = input("Enter Email: ")

        if "@" in email and "." in email:
            return email

        print("Please enter a valid email address.")
# ==========================================
# Display one student
# ==========================================
def display_student(student):

    print("Student ID :", student["id"])
    print("Name       :", student["name"])
    print("Age        :", student["age"])
    print("Gender     :", student["gender"])
    print("Phone      :", student["phone"])
    print("Email      :", student["email"])
    print("Course     :", student["course"])
    print("Year       :", student["year"])
    print("Address    :", student["address"])
    print("--------------------------------------")
# ==========================================
# Add a new student
# ==========================================
def add_student(students):

    student_id = input("Enter Student ID: ").strip()

    if student_id == "":
        print("Student ID cannot be empty.")
        return

    # Check duplicate ID
    for student in students:

        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Student Name: ").strip()

    if name == "":
        print("Student Name cannot be empty.")
        return

    age = get_valid_age()

    gender = input("Enter Gender: ").strip()

    if gender == "":
        print("Gender cannot be empty.")
        return

    phone = get_valid_phone()

    email = get_valid_email()

    course = input("Enter Course: ").strip()

    if course == "":
        print("Course cannot be empty.")
        return

    year = input("Enter Year: ").strip()

    if year == "":
        print("Year cannot be empty.")
        return

    address = input("Enter Address: ").strip()

    if address == "":
        print("Address cannot be empty.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "email": email,
        "course": course,
        "year": year,
        "address": address
    }

    students.append(student)

    save_students(students)

    print("\nStudent added successfully.")
# ==========================================
# View all students
# ==========================================

def view_students(students):

    if not students:
        print("No students found.")
        return

    print("\n========== STUDENT DETAILS ==========")

    for student in students:
        display_student(student)
# ==========================================
# Search by Student ID
# ==========================================
def search_by_id(students):

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found!")
            display_student(student)
            return

    print("Student not found.")
# ==========================================
# Search by Student Name
# ==========================================
def search_by_name(students):

    name = input("Enter Student Name: ").strip().lower()

    found = False

    for student in students:

        if name in student["name"].lower():

            print("\nStudent Found!")
            display_student(student)

            found = True

    if not found:
        print("No student found with that name.")
# ==========================================
# Search by Course
# ==========================================
def search_by_course(students):

    course = input("Enter Course: ").strip().lower()

    found = False

    for student in students:

        if student["course"].lower() == course:

            print("\nStudent Found!")
            display_student(student)

            found = True

    if not found:
        print("No students found in this course.")
# ==========================================
# Search menu
# ==========================================
def search_student(students):

    while True:

        print("\n========== SEARCH ==========")
        print("1. Search by ID")
        print("2. Search by Name")
        print("3. Search by Course")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_by_id(students)

        elif choice == "2":
            search_by_name(students)

        elif choice == "3":
            search_by_course(students)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")
# ==========================================
# Update student
# ==========================================
def update_student(students):

    student_id = input("Enter Student ID to update: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("\nEnter new details:")

            name = input("Enter Name: ").strip()

            if name != "":
                student["name"] = name

            student["age"] = get_valid_age()

            gender = input("Enter Gender: ").strip()

            if gender != "":
                student["gender"] = gender

            student["phone"] = get_valid_phone()

            student["email"] = get_valid_email()

            course = input("Enter Course: ").strip()

            if course != "":
                student["course"] = course

            year = input("Enter Year: ").strip()

            if year != "":
                student["year"] = year

            address = input("Enter Address: ").strip()

            if address != "":
                student["address"] = address

            save_students(students)

            print("Student updated successfully.")
            return

    print("Student not found.")
# ==========================================
# Delete student
# ==========================================
def delete_student(students):

    student_id = input("Enter Student ID to delete: ").strip()

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            save_students(students)

            print("Student deleted successfully.")
            return

    print("Student not found.")
# ==========================================
# Sort students by name
# ==========================================
def sort_students(students):

    if not students:
        print("No students found.")
        return

    students.sort(key=lambda student: student["name"].lower())

    save_students(students)

    print("\nStudents sorted by name.")

    view_students(students)
# ==========================================
# Student statistics
# ==========================================
def student_statistics(students):

    if not students:
        print("No students found.")
        return

    total_students = len(students)

    courses = {}

    for student in students:

        course = student["course"]

        if course in courses:
            courses[course] += 1
        else:
            courses[course] = 1

    print("\n========== STUDENT STATISTICS ==========")

    print("Total Students :", total_students)

    print("\nStudents by Course:")

    for course in courses:
        print(course, ":", courses[course])
# ==========================================
# Main program
# ==========================================
def main():

    students = load_students()

    while True:

        print("\n==========================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("==========================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort Students")
        print("7. Student Statistics")
        print("8. Exit")

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
            sort_students(students)

        elif choice == "7":
            student_statistics(students)

        elif choice == "8":
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")
# ==========================================
# Run the program
# ==========================================
if __name__ == "__main__":
    main()

