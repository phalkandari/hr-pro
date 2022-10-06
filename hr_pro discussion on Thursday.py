from sre_parse import GLOBAL_FLAGS


class Employee:
    """A simple employee class."""

    def __init__(self, name, age, salary, employment_years):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_years = employment_years

    def __str__(self):
        """returns the string representation of the object."""
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Employment Years: {self.employment_years}"

    def get_annual_salary(self):
        """describes the annual salary of an employee."""
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
        super().__init__(name, age, salary, employment_years)
        self.bonus_percentage = bonus_percentage

    def __str__(self):
        return super().__str__()+f" Bonus: {self.bonus_percentage}"

    def get_bonus(self):
        return self.bonus_percentage * self.salary


def main():
    employees_list = []
    managers_list = []
    print('''Options:
          1. Show Employees
          2. Show Managers
          3. Add An Employee
          4. Add A Manager
          5. Exit''')

    choice = int(input("What would you like to do? "))

    if choice == 1:
        for employee in employees_list:
            print(employee)
    elif choice == 2:
        for manager in managers_list:
            print(manager)
    elif choice == 3:
        name = input("Name: ")
        age = int(input("Age: "))
        salary = int(input("Salary: "))
        employment_years = int(input("Employment years: "))
        added_employee = Employee(name, age, salary, employment_years)
        employees_list.append(added_employee)
        print("Employee added successfully")
        print(added_employee)
    elif choice == 4:
        name = input("Name: ")
        age = int(input("Age: "))
        salary = int(input("Salary: "))
        employment_years = int(input("Employment years: "))
        bonus_percentage = float(input("Bonus Percentage: "))
        added_manager = Manager(
            name, age, salary, employment_years, bonus_percentage)
        managers_list.append(added_manager)
        print("Manager added successfully")
        print(added_manager)
    else:
        print("Invalid input!")


if __name__ == '__main__':
    main()
