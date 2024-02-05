import json
json_file = "employees.json"
employees = []

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
    def __str__(self):
        return f'Name: {self.name} Salary: {self.salary}'

if __name__ == '__main__':
    with open(json_file, 'r') as file:
        data = json.load(file)
        for item in data:
            e = Employee(item["name"], item["salary"])
            employees.append(e)

    for e in employees:
        print(f'Before: {e}')
        e.salary = e.salary + 10
        print(f'After: {e}')

    with open(json_file, 'w') as file:
        employee_data = [{'name': e.name, 'salary': e.salary} for e in employees]
        json.dump(employee_data, file, indent=4)