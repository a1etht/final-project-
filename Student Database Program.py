#Programmer: Alethea Lo & Matthew Anderson
#Date: 5/13/2025
#Student Database Program
import sqlite3

#Connecting to the database
conn = sqlite3.connect('students.db')
c = conn.cursor()


def view_all_students():
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    for row in rows:
        print(row)

def edit_student(student_id):
    print("Which field do you want to edit?")
    field = input("first_name, last_name, age, major, email, gpa: ").strip()
    if field not in ['first_name', 'last_name', 'age', 'major', 'email', 'gpa']:
        print("Invalid field.")
        return
    new_value = input(f"Enter new value for {field}: ")
    c.execute(f"UPDATE students SET {field} = ? WHERE id = ?", (new_value, student_id))
    conn.commit()
    print("Student updated.")

def main():
    while True:
        print("\n1. View All Students")
        print("2. Edit Student")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            view_all_students()
        elif choice == '2':
            student_id = int(input("Enter student ID to edit: "))
            edit_student(student_id)
        elif choice == '3':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
