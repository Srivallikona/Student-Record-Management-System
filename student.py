
from database import connect_db

def add_student():
    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    course = input("Enter student course: ").strip()

    if not name or not age or not course:
        print("All fields are required!")
        return

    try:
        age = int(age)

        if age <= 0:
            print("Age must be greater than zero!")
            return

        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
            (name, age, course)
        )

        connection.commit()
        connection.close()

        print("Student added successfully!")

    except ValueError:
        print("Please enter a valid number for age.")

def view_students():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    connection.close()

    if not students:
        print("No student records found!")
        return

    print("\n----- STUDENT RECORDS -----")

    for student in students:
        print("ID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])
        print("--------------------------")

def search_student():
    student_id = input("Enter student ID to search: ")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    connection.close()

    if student:
        print("\nStudent Found!")
        print("ID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])
    else:
        print("Student not found!")

def update_student():
    student_id = input("Enter student ID to update: ")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("Current Name:", student[1])
        print("Current Age:", student[2])
        print("Current Course:", student[3])

        name = input("Enter new name: ").strip()
        age = input("Enter new age: ").strip()
        course = input("Enter new course: ").strip()

        if not name or not age or not course:
            print("All fields are required!")
            connection.close()
            return

        try:
            age = int(age)

            if age <= 0:
                print("Age must be greater than zero!")
                connection.close()
                return

            cursor.execute(
                """UPDATE students
                   SET name = ?, age = ?, course = ?
                   WHERE student_id = ?""",
                (name, age, course, student_id)
            )

            connection.commit()
            print("Student updated successfully!")

        except ValueError:
            print("Please enter a valid number for age.")

    else:
        print("Student not found!")

    connection.close()

def delete_student():
    student_id = input("Enter student ID to delete: ")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("Student Name:", student[1])

        confirm = input("Are you sure you want to delete? (yes/no): ").lower()

        if confirm == "yes":
            cursor.execute(
                "DELETE FROM students WHERE student_id = ?",
                (student_id,)
            )

            connection.commit()
            print("Student deleted successfully!")
        else:
            print("Deletion cancelled!")

    else:
        print("Student not found!")

    connection.close()
