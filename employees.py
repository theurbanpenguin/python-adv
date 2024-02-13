from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    @abstractmethod
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