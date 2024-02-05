class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

if __name__ == '__main__':
    employees = [
        Employee("Vera", 2000, "Roadhouse Manager"),
        Employee("Chuck", 1800, "Table Waiter"),
        Employee("Samantha", 1800, "Table Waiter"),
        Employee("Roberto", 2100, "Kitchen Chef"),
        Employee("Dave", 2200, "Car Mechanic"),
        Employee("Tina", 2300, "Car Mechanic"),
        Employee("Ringo", 1900, "Car Mechanic")
    ]

    for e in employees:
        print(f"{e.name}: £{e.salary}: {e.job_title}")