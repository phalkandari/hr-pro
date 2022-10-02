class Employee:
    """A simple employee class"""
    def __init__(self, name, age, salary, employment_years):
       self.name = name
       self.age = age
       self.salary = salary
       self.employment_years = employment_years
       
    def get_annual_salary(self, salary):
        """describes the annual salary/payment of an employee"""
        return self.salary * 12
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Employment Years: {self.employment_years}"

class Manager(Employee):
    def __init__(self, name, age, salary, employment_years, bonus_percentage):
         super().__init__(name, age, salary, employment_years)
         self.bonus_percentage = self.bonus_percentage * self.salary
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Employment Years: {self.employment_years}, Bonus Percentage: {self.bonus_percentage}"

#employees
employee_one = Employee("Laila", 24, 9999, 4)
employee_two = Employee("Moh", 27, 999, 2)

#managers
manager_one = Manager("sammy", 52, 4600, 19, 1380.0)


employee_list = []
manager_list = []







def main():
	# main code here

if __name__ == '__main__':
	main()
