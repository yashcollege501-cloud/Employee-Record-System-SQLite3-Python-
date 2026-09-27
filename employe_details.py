import sqlite3

# Establish connection and cursor
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    salary INTEGER,
    mobile TEXT
)""")
conn.commit()

def add_employees():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        department = input("Enter Department: ")
        salary = int(input("Enter salary: "))
        mobile = input("Enter Mobile Number: ")
        
        cursor.execute("""
        INSERT INTO employees (name, age, department, salary, mobile) 
        VALUES (?, ?, ?, ?, ?)""", (name, age, department, salary, mobile))
        conn.commit()
        print("Employee added successfully!")
    except ValueError:
        print("Invalid input! Age and Salary must be integers.")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    
    if not employees:
        print("No Employees found!")
        return
        
    print("\nID  | NAME                 | AGE | DEPARTMENT         | SALARY     | MOBILE")
    print("-" * 80)
    for emp in employees:
        # Formatted string for a clean table view
        print(f"{emp[0]:<3} | {emp[1]:<20} | {emp[2]:<3} | {emp[3]:<18} | {emp[4]:<10} | {emp[5]}")

def search_employees():
    try:
        emp_id = int(input("Enter employee ID: "))
        cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
        employee = cursor.fetchone()
        
        if employee:
            print("\nEmployee Found:")
            print(f"ID:         {employee[0]}")
            print(f"Name:       {employee[1]}")
            print(f"Age:        {employee[2]}")
            print(f"Department: {employee[3]}")
            print(f"Salary:     {employee[4]}")
            print(f"Mobile:     {employee[5]}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid ID format! ID must be an integer.")

def update_employee():
    try:
        emp_id = int(input("Enter employee ID to update: "))
        cursor.execute("SELECT * FROM employees WHERE id=?", (emp_id,))
        employee = cursor.fetchone()
        
        if not employee:
            print("Employee Not Found")
            return
            
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        department = input("Enter new Department: ")
        salary = int(input("Enter new salary: "))
        mobile = input("Enter new Mobile Number: ")
        
        cursor.execute("""
        UPDATE employees 
        SET name=?, age=?, department=?, salary=?, mobile=? 
        WHERE id=?""", (name, age, department, salary, mobile, emp_id))
        conn.commit()
        print("Employee Updated Successfully!")
    except ValueError:
        print("Invalid input! Age, Salary, and ID must be integers.")

def delete_employee():
    try:
        emp_id = int(input("Enter employee ID to Delete: "))
        cursor.execute("SELECT name FROM employees WHERE id=?", (emp_id,))
        employee = cursor.fetchone()
        
        if not employee:
            print("Employee not found!")
            return
            
        confirm = input(f"Are you sure you want to delete {employee[0]}? (y/n): ")
        if confirm.lower() == "y":
            cursor.execute("DELETE FROM employees WHERE id=?", (emp_id,))
            conn.commit()
            print("Employee deleted successfully!")
        else:
            print("Deletion Cancelled.")
    except ValueError:
        print("Invalid ID format!")

# Main Loop
try:
    while True:
        print("\n============ EMPLOYEE RECORD SYSTEM ================")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        print("====================================================")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employees()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employees()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Thank you for using Employee Record System!")
            break
        else:
            print("Invalid choice. Please try again.")
finally:
    # This guarantees the connection always closes when exiting or crashing
    conn.close()

#OUTPUT:-

# ============ EMPLOYEE RECORD SYSTEM ================
# 1. Add Employee
# 2. View Employees
# 3. Search Employee
# 4. Update Employee
# 5. Delete Employee
# 6. Exit
# ====================================================
# Enter your choice: 1
# Enter name: Yash D. Dhawale
# Enter age: 22
# Enter Department: 22000
# Enter salary: 
# PS Y:\> ^C
# PS Y:\> 
# PS Y:\>  y:; cd 'y:\\'; & 'c:\Users\dhawa\AppData\Local\Programs\Python\Python312\python.exe' 'c:\Users\dhawa\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\launcher' '64362' '--' 'Y:\employe_details.py' 

# ============ EMPLOYEE RECORD SYSTEM ================
# 1. Add Employee
# 2. View Employees
# 3. Search Employee
# 4. Update Employee
# 5. Delete Employee
# 6. Exit
# ====================================================
# Enter your choice: 1
# Enter name: Yash D.Dhawale
# Enter age: 22
# Enter Department: Developar
# Enter salary: 22000
# Enter Mobile Number: 8983744221
# Employee added successfully!

# ============ EMPLOYEE RECORD SYSTEM ================
# 1. Add Employee
# 2. View Employees
# 3. Search Employee
# 4. Update Employee
# 5. Delete Employee
# 6. Exit
# ====================================================
# Enter your choice: 1
# Enter name: Deep D.Dhawale
# Enter age: 22
# Enter Department: Mech ENG
# Enter salary: 20000
# Enter Mobile Number: 7028626224
# Employee added successfully!

# ============ EMPLOYEE RECORD SYSTEM ================
# 1. Add Employee
# 2. View Employees
# 3. Search Employee
# 4. Update Employee
# 5. Delete Employee
# 6. Exit
# ====================================================
# Enter your choice: 2

# ID  | NAME                 | AGE | DEPARTMENT         | SALARY     | MOBILE
# --------------------------------------------------------------------------------
# 1   | Yash D.Dhawale       | 22  | Developar          | 22000      | 8983744221
# 2   | Deep D.Dhawale       | 22  | Mech ENG           | 20000      | 7028626224

# ============ EMPLOYEE RECORD SYSTEM ================
# 1. Add Employee
# 2. View Employees
# 3. Search Employee
# 4. Update Employee
# 5. Delete Employee
# 6. Exit
# ====================================================
# Enter your choice: 3
# Enter employee ID: 1

# Employee Found:
# ID:         1
# Name:       Yash D.Dhawale
# Age:        22
# Department: Developar
# Salary:     22000
# Mobile:     8983744221

# ============ EMPLOYEE RECORD SYSTEM ================
# 1. Add Employee
# 2. View Employees
# 3. Search Employee
# 4. Update Employee
# 5. Delete Employee
# 6. Exit
# ====================================================
# Enter your choice: 4
# Enter employee ID to update: 2
# Enter new name: Sarthak Mundekar
# Enter new age: 23
# Enter new Department: Testing
# Enter new salary: 25000
# Enter new Mobile Number: 9865254250 
# Employee Updated Successfully!

# ============ EMPLOYEE RECORD SYSTEM ================
# 1. Add Employee
# 2. View Employees
# 3. Search Employee
# 4. Update Employee
# 5. Delete Employee
# 6. Exit
# ====================================================
# Enter your choice: 2

# ID  | NAME                 | AGE | DEPARTMENT         | SALARY     | MOBILE
# --------------------------------------------------------------------------------
# 1   | Yash D.Dhawale       | 22  | Developar          | 22000      | 8983744221
# 2   | Sarthak Mundekar     | 23  | Testing            | 25000      | 9865254250

# ============ EMPLOYEE RECORD SYSTEM ================
# 1. Add Employee
# 2. View Employees
# 3. Search Employee
# 4. Update Employee
# 5. Delete Employee
# 6. Exit
# ====================================================
# Enter your choice: 5
# Enter employee ID to Delete: 2
# Are you sure you want to delete Sarthak Mundekar? (y/n): y
# Employee deleted successfully!

# ============ EMPLOYEE RECORD SYSTEM ================
# 1. Add Employee
# 2. View Employees
# 3. Search Employee
# 4. Update Employee
# 5. Delete Employee
# 6. Exit
# ====================================================
# Enter your choice: 2

# ID  | NAME                 | AGE | DEPARTMENT         | SALARY     | MOBILE
# --------------------------------------------------------------------------------
# 1   | Yash D.Dhawale       | 22  | Developar          | 22000      | 8983744221

# ============ EMPLOYEE RECORD SYSTEM ================
# 1. Add Employee
# 2. View Employees
# 3. Search Employee
# 4. Update Employee
# 5. Delete Employee
# 6. Exit
# ====================================================
# Enter your choice: 6
# Thank you for using Employee Record System!
