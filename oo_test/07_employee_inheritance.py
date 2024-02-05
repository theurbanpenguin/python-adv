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
 
Mechanic
if __name__ == '__main__':
    employees = [
        Manager("Vera", 2000),
        Waiter("Chuck", 1800),
        Waiter("Samantha", 1800),
        Chef("Roberto", 2100),
        Mechanic("Dave", 2200),
        Mechanic("Tina", 2300),
        Mechanic("Ringo", 1900)
    ]

    for e in employees:
        print(f"{e.name}: £{e.salary}: {e.job_title}")

    for e in employees:
        if isinstance(e, Waiter):
            print(f"{e.name}: £{e.salary}: {e.job_title}")

    Mechanic.job_title = "Spanner Man"
    for e in employees:
        print(f"{e.name}: £{e.salary}: {e.job_title}")
