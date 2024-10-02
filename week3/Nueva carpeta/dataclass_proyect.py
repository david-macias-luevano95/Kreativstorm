from dataclasses import dataclass
employee_list = []


@dataclass
class Employee:
    name: str
    age: int
    department: str
    salary: float

# Create an empty list to store employee objects
employee_list = []

def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    department = input("Enter employee department: ")
    salary = float(input("Enter employee salary: "))
    employee = Employee(name, age, department, salary)
    employee_list.append(employee)
    print(f"{name} has been added to the system.")

def display_employees():
    print("\n Employee Details:")
    for index, employee in enumerate(employee_list, start=1):
        print(f"Employee {index}:")
        print(f"Name: {employee.name}")
        print(f"Age: {employee.age}")
        print(f"Department: {employee.department}")
        print(f"Salary: {employee.salary}")
        print("-" * 20)

def update_employee():
    name = input("Enter the name of the employee you want to update: ")
    for employee in employee_list:
        if employee.name == name:
            new_salary = float(input("Enter the new salary: "))
            employee.salary = new_salary
            print(f"{employee.name}'s salary has been updated to {new_salary}.")
            return
    print(f"No employee with the name '{name}' found in the system.")

def remove_employee():
    name = input("Enter the name of the employee you want to remove: ")
    for employee in employee_list:
        if employee.name == name:
            employee_list.remove(employee)
            print(f"{employee.name} has been removed from the system.")
            return
    print(f"No employee with the name '{name}' found in the system.")

# Main program loop
while True:
    print("\nEmployee Management System Menu:")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Update Employee Salary")
    print("4. Remove Employee")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        display_employees()
    elif choice == '3':
        update_employee()
    elif choice == '4':
        remove_employee()
    elif choice == '5':
        print("Exiting Employee Management System.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
