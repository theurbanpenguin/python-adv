import json
json_file = "employees.json"
employees = []
class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def __str__(self) -> str:
        return f'Name: {self.name} Salary: {self.salary}'

if __name__ == '__main__':
    with open(json_file, 'r') as file:
        data = json.load(file)
        for item in data:
            e = Employee(item["name"], item["salary"])
            employees.append(e)
    for e in employees:
        print(e)

