from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
    @abstractmethod
    def __str__(self):
        pass
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
if __name__ == '__main__':
    employees: list = [
        Manager("Vera", 2000),
        Waiter("Chuck", 1800),
        Waiter("Samantha", 1800),
        Chef("Roberto", 2100),
        Mechanic("Dave", 2200),
        Mechanic("Tina", 2300),
        Mechanic("Ringo", 1900),
        Waiter("Bob", 2105)
    ]
for e in employees:
        print(e)