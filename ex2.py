import sqlite3
DB_NAME = "test.db"
def get_connection():
    """Helper function to connect to the database."""
    return sqlite3.connect(DB_NAME)
def create_table():
    """Create the COMPANY table if it doesn't exist."""
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS COMPANY (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            address TEXT,
            salary REAL
        );
    """)
    conn.commit()
    conn.close()
    print("Table ready.")

def insert_employee():
    """Insert a new employee using user input."""
    conn = get_connection()
    cur = conn.cursor()

    print("\nEnter new employee details.")
    name = input("Name: ")
    age = int(input("Age: "))
    address = input("Address: ")
    salary = float(input("Salary: "))

    cur.execute(
        "INSERT INTO COMPANY (name, age, address, salary) VALUES (?, ?, ?, ?);",
        (name, age, address, salary)
    )
    conn.commit()
    print("Employee added with id:", cur.lastrowid)

    conn.close()

def delete_employee():
    """Delete an employee by ID using user input."""
    conn = get_connection()
    cur = conn.cursor()

    emp_id = int(input("Enter employee ID to delete: "))
    confirm = input(f"Are you sure you want to delete ID {emp_id}? (y/n): ").lower()

    if confirm == "y":
        cur.execute("DELETE FROM COMPANY WHERE id = ?;", (emp_id,))
        conn.commit()
        print("Rows deleted:", conn.total_changes)
    else:
        print("Delete cancelled.")

    conn.close()

def main():
    """Main menu loop."""
    create_table()  # Ensure table exists

    while True:
        print("\n=== COMPANY DATABASE MENU ===")
        print("1. Add employee (INSERT)")
        print("2. Delete employee (DELETE)")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            insert_employee()
        elif choice == "2":
            delete_employee()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
