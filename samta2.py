import mysql.connector

# Function to connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",  # Replace with your MySQL password
            database="school"
        )
        print("Database connection successful")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to create a new student record
def insert_student(cursor, first_name, last_name, age, grade):
    try:
        query = "INSERT INTO students (first_name, last_name, age, grade) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (first_name, last_name, age, grade))
        print("Student inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to update a student's grade
def update_student_grade(cursor, first_name, new_grade):
    try:
        query = "UPDATE students SET grade = %s WHERE first_name = %s"
        cursor.execute(query, (new_grade, first_name))
        print("Student grade updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to delete a student record
def delete_student(cursor, last_name):
    try:
        query = "DELETE FROM students WHERE last_name = %s"
        cursor.execute(query, (last_name,))
        print("Student deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to fetch and display all student records
def fetch_all_students(cursor):
    try:
        query = "SELECT * FROM students"
        cursor.execute(query)
        results = cursor.fetchall()
        for (student_id, first_name, last_name, age, grade) in results:
            print(f"ID: {student_id}, Name: {first_name} {last_name}, Age: {age}, Grade: {grade}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Main function to perform all operations
def main():
    db = connect_to_database()
    if db is None:
        return

    cursor = db.cursor()
    
    # Insert a new student
    insert_student(cursor, "Alice", "Smith", 18, 95.5)
    db.commit()
    
    # Update the grade of the student with first name "Alice"
    update_student_grade(cursor, "Alice", 97.0)
    db.commit()
    
    # Delete the student with last name "Smith"
    delete_student(cursor, "Smith")
    db.commit()
    
    # Fetch and display all student records
    fetch_all_students(cursor)
    
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
