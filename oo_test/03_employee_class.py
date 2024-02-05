class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

if __name__ == '__main__':
    e = Employee("Vera", 2000)
    print(f"{e.name}: £{e.salary}")