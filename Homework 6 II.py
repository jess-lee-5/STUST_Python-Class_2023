class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("\n")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: ${self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime_hours = hours_worked - 50
            overtime_amount = overtime_hours * (self.emp_salary / 50)
            total_salary = self.emp_salary + overtime_amount
            return total_salary
        else:
            return self.emp_salary

employees = [
             Employee("ADAMS", "E7876", 50000, "ACCOUNTING"),
             Employee("JONES", "E7499", 45000, "RESEARCH"),
             Employee("MARTIN", "E7900", 50000, "SALES"),
             Employee("SMITH", "E7698", 55000, "OPERATIONS")
            ]
            
for emp in employees:
    emp.print_employee_details()
    print("Calculating salary with overtime:")
    salary_with_overtime = emp.calculate_emp_salary(55)
    print(f"Total Salary with Overtime: ${salary_with_overtime:.0f}\n")

    employees[2].assign_department("HR")
    print("Updated department of ALL:")
    employees[2].print_employee_details()