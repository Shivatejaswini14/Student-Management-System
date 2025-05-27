import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create students table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')
conn.commit()

def add_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print("Student added successfully.\n")

def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
    print()

def update_student(student_id, name, age, grade):
    cursor.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, student_id))
    conn.commit()
    print("Student updated successfully.\n")

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("Student deleted successfully.\n")

def search_student(student_id):
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    row = cursor.fetchone()
    if row:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}\n")
    else:
        print("Student not found.\n")

def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student by ID")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            add_student(name, age, grade)
        
        elif choice == "2":
            view_students()

        elif choice == "3":
            id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            grade = input("Enter new grade: ")
            update_student(id, name, age, grade)

        elif choice == "4":
            id = int(input("Enter student ID to delete: "))
            delete_student(id)

        elif choice == "5":
            id = int(input("Enter student ID to search: "))
            search_student(id)

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
    conn.close()
