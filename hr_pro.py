class Employee:
    """A simple employee class."""
    def __init__(self, name, age, salary, employment_years):
       self.name = name
       self.age = age
       self.salary = salary
       self.employment_years = employment_years
       
    def get_annual_salary(self, salary):
        """describes the annual salary of an employee."""
        return self.salary * 12
    
    def __str__(self):
        """returns the string representation of the object."""
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Employment Years: {self.employment_years}"

class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
         super().__init__(name, age, salary, employment_years)
         self.bonus_percentage = bonus_percentage * self.salary
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Employment Years: {self.employment_years}, Bonus Percentage: {self.bonus_percentage}"

#employees
employee_one = Employee("Laila", 24, 9999, 4)
employee_two = Employee("Moh", 27, 999, 2)

#managers
manager_one = Manager("sammy", 52, 4600, 19, 1380)

def get_options():
    return ["Show Employees", "Show Managers", "Add An Employee", "Add A Manager", "Exit"]


def show_options(options):
    print()
    print("Options:")

    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

    print()


def HR_Pro():
    print("Welcome to HR Pro")
    print("Options: ")





# def showing_employees():
    
# def showing_managers():
    
def adding_an_employee(employees):
    employee_list = [employee_one, employee_two]
    for employee in employees:
        employee_list.append(employee)
    
    
def adding_a_manager(managers):
    manager_list = [manager_one]
    for manager in managers:
        manager_list.append(manager)


# def Exiting():
    
    
    
    
    
    








def main():
    print(
        "Welcome to HR Pro"
        "Options:"
    )
    options = get_options()

# if __name__ == '__main__':
# 	main()
