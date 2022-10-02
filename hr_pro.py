from sre_parse import GLOBAL_FLAGS


class Employee:
    """A simple employee class."""
    def __init__(self, name, age, salary, employment_years):
       self.name = name
       self.age = age
       self.salary = salary
       self.employment_years = employment_years
       
    def get_annual_salary(self, salary):
        """describes the annual salary of an employee."""
        self.salary = salary
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
manager_one = Manager("sammy", 52, 4600, 19, 1380.0)


#To itirate over each option and number it
def get_options():
    return ["Show Employees", "Show Managers", "Add An Employee", "Add A Manager", "Exit"]


def show_options(options):
    print()
    print("Options:")

    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

    print()

employee_list = [employee_one, employee_two]
manager_list = [manager_one]

#The Function asking the user to choose an option
def asking_for_user_option():
    option = int(input("What would you like to do? "))
    if option == 1:
        show_employees()
    elif option == 2:
        show_managers()
    elif option == 3:
        add_an_employee(employee_list)
    elif option == 4:
        add_a_manager(manager_list)
    elif option == 5:
        Exit()

#The Function 1
def show_employees():
    print("Employees")
    print(" ")
    print (employee_list)

#The Function 2
def show_managers():
    print("Managers")
    print(" ")
    print (manager_list)
    
#The Function 3
def add_an_employee(employee_list):
    name = input("Name: ")
    age = int(input("Age: "))
    salary = int(input("Salary: "))
    employment_years = int(input("Employment years: "))
    added_employee = Employee(name, age, salary, employment_years)
    employee_list.append(added_employee)
    print("Employee added successfully")
    print(added_employee)
    return employee_list

#The Function 4
def add_a_manager(manager_list):
    name = input("Name: ")
    age = int(input("Age: "))
    salary = int(input("Salary: "))
    employment_years = int(input("Employment years: "))
    bonus_percentage = float(input("Bonus Percentage: "))
    added_manager = Manager(name, age, salary, employment_years, bonus_percentage)
    manager_list.append(added_manager)
    print("Manager added successfully")
    print(added_manager)
    return manager_list

#The Function 5
def Exit():
    quit()    



def main():
    print("Welcome to HR Pro")
    print("Options:")
    show_options(get_options())
    asking_for_user_option()

if __name__ == '__main__':
	main()

print (employee_one)