class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    job_title = "Roadhouse Manager"


class Waiter(Employee):
    job_title = "Table Waiter"


class Chef(Employee):
    job_title = "Kitchen Chef"


class Mechanic(Employee):
    job_title = "Car Mechanic"
