
from database import create_table
from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

def main():
    create_table()

    while True:
        print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using Student Record Management System!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
