class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

if __name__ == '__main__':
    employees = [
        Employee("Vera", 2000, "Manager"),
        Employee("Chuck", 1800, "Waiter"),
        Employee("Samantha", 1800, "Waiter"),
        Employee("Roberto", 2100, "Chef"),
        Employee("Dave", 2200, "Mechanic"),
        Employee("Tina", 2300, "Mechanic"),
        Employee("Ringo", 1900, "Mechanic")
    ]

    for e in employees:
        print(f"{e.name}: £{e.salary}: {e.job_title}")