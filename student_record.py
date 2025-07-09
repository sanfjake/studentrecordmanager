import sqlite3
import re

DB_NAME = "students.db"

# Connect and create the students table
def initialize_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            grade TEXT NOT NULL,
                            email TEXT NOT NULL)''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# Add a new student
def add_student():
    try:
        name = input("Enter student's name: ")
        grade = input("Enter student's grade: ")
        email = input("Enter student's email: ")
        if '@' not in email:
            print("Invalid email format.")
            return
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, grade, email) VALUES (?, ?, ?)", (name, grade, email))
        conn.commit()
        conn.close()
        print("Student added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")

# View all students
def view_students():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()
        conn.close()

        if not records:
            print("No records found.")
        else:
            for row in records:
                print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}, Email: {row[3]}")
    except sqlite3.Error as e:
        print(f"Error retrieving students: {e}")

# Update student record
def update_student():
    try:
        student_id = int(input("Enter the ID of the student to update: "))
        new_name = input("Enter new name: ")
        new_grade = input("Enter new grade: ")
        new_email = input("Enter new email: ")
        if '@' not in new_email:
            print("Invalid email format.")
            return
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET name = ?, grade = ?, email = ? WHERE id = ?", 
                       (new_name, new_grade, new_email, student_id))
        conn.commit()
        conn.close()
        print("Student record update successful.")
    except sqlite3.Error as e:
        print(f"Error updating student: {e}")
    except ValueError:
        print("Invalid ID. Must be an integer.")

# Delete student record
def delete_student():
    try:
        student_id = int(input("Enter the ID of the student to be deleted: "))
        confirm = input(f"Are you sure you want to delete student ID {student_id}? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Deletion cancelled.")
            return
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        conn.close()
        print("Student deletion successful.")
    except sqlite3.Error as e:
        print(f"Error deleting student: {e}")
    except ValueError:
        print("Invalid ID. Must be a valid student ID number.")

# Menu
def main():
    initialize_db()
    while True:
        print("\nStudent Record Manager")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()


# -----------------------------
# References
# -----------------------------

# Study.com. (n.d.). *Python SQLite: Creating a Database & Table*. Retrieved July 9, 2025, 
# from https://study.com/academy/lesson/python-sqlite-creating-a-database-table.html

# Python Software Foundation. (n.d.). *sqlite3 — DB-API 2.0 interface for SQLite databases*. 
# Retrieved July 9, 2025, from https://docs.python.org/3/library/sqlite3.html

# W3Schools. (n.d.). *Python SQLite*. Retrieved July 9, 2025, from https://www.w3schools.com/sql/sql_python.asp

# GeeksforGeeks. (2021, September 21). *Python SQLite - Create a new database*. 
# Retrieved from https://www.geeksforgeeks.org/python-sqlite-create-a-new-database/

# OpenAI. (2025). ChatGPT [Large language model]. https://chat.openai.com/
