class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f'{self.name}: {self.salary}'

if __name__ == '__main__':
    employees: list = [
        Employee("Vera", 2000),
        Employee("Chuck", 1800),
        Employee("Samantha", 1800),
        Employee("Roberto", 2100),
        Employee("Dave", 2200),
        Employee("Tina", 2300),
        Employee("Ringo", 1900),
        Employee("Bob", 2105)
    ]
for e in employees:
        print(e)