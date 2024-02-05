class Employee:
    def __init__(self, first_name, last_name, salary, shift
        self._first_name = first_name
        self._last_name = last_name
        self._salary = salary
        self.shift = shift

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

    def get_salary(self):
        return f"{self._salary}"

    def set_salary(self, amount):
        ''' Do not allow more than 20% increase '''
        if amount > self._salary * 0.20:
            print("Pay increase cannot be more than 20%")
            return
        elif amount < 0:
            print("Pay increases cannot allow reductions in pay")
            return
        self._salary = self._salary + amount

class Manager(Employee):
    job_title = "Roadhouse Manager"


class Waiter(Employee):
    job_title = "Table Waiter"


class Chef(Employee):
    job_title = "Kitchen Chef"


class Mechanic(Employee):
    job_title = "Car Mechanic"
