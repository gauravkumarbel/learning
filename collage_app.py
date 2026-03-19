# Gaurav Kumar College App

class Student:
    def __init__(self, name, student_class):
        self.name = name
        self.student_class = student_class
        self.subjects = ["Science", "Math", "English"]
        self.fee = 1000

    def display_info(self):
        print("\n----- Student Details -----")
        print(f"Name: {self.name}")
        print(f"Class: {self.student_class}")
        print(f"Subjects: {', '.join(self.subjects)}")
        print(f"Monthly Fee: ₹{self.fee}")
        print("---------------------------\n")


class CollegeApp:
    def __init__(self):
        self.college_name = "Gaurav Kumar College"
        self.students = []

    def show_menu(self):
        print(f"\nWelcome to {self.college_name}")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

    def add_student(self):
        name = input("Enter student name: ")
        student_class = int(input("Enter class (8-12): "))

        if student_class < 8 or student_class > 12:
            print("❌ Only classes 8 to 12 allowed!")
            return

        student = Student(name, student_class)
        self.students.append(student)
        print("✅ Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found!")
            return

        for student in self.students:
            student.display_info()


# Run App
app = CollegeApp()

while True:
    app.show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        app.add_student()
    elif choice == "2":
        app.view_students()
    elif choice == "3":
        print("Exiting App...")
        break
    else:
        print("Invalid choice! Try again.")
