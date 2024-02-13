class Employee():
    def __init__(self, firstname: str, lastname: str, salary: int):
        self._firstname = firstname
        self._lastname = lastname
        self._salary = salary

    @property
    def name(self):
        return f'{self._firstname.capitalize()} {self._lastname.capitalize()}'

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount: int):
        if amount < self._salary * 0.2:
            self._salary = self._salary + amount
        else:
            print("The amount is to high")

    def __str__(self):
        return "You should not have done this"
class Manager(Employee):
    job_title = "Manager"
    def __str__(self):
        return f'{self.name}: {self.salary}, {self.job_title}'
class Waiter(Employee):
    job_title = "Table Waiter"
    def __str__(self):
        return f'{self.name}: {self.salary}, {self.job_title}'
class Chef(Employee):
    job_title = "Kitchen Chef"
    def __str__(self):
        return f'{self.name}: {self.salary}, {self.job_title}'
class Mechanic(Employee):
    job_title = "Car Mechanic"
    def __str__(self):
        return f'{self.name}: {self.salary}, {self.job_title}'