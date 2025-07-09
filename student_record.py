import sqlite3
import re

DB_name = "students.db"

# Connect and create the students table
def initialize_db():
    try:
        conn = sqlite3.connect(DN_NAME)
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT
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
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    if not records:
        print("No records found.")
    else:
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1], Grade: {row[2]}, Email: {row[3]}}")

# Update student record
def update_student():
    try:
        student_id = int(input("Enter the ID of the student to update: "))
    except ValueError:
