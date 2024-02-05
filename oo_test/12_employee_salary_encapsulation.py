from employee import Manager
from employee import Waiter
from employee import Chef
from employee import Mechanic

def print_account_report():
    print("Accounting")
    print("==========")
    for e in employees:
        print(f"{e.get_full_name()}: £{e.get_salary()}")

def print_staffing_report():
    print("Staffing")
    print("==========")
    for e in employees:
        print(f"{e.get_full_name()}: {e.job_title}")

def raise_salary(employee, amount):
    for e in employees:
        employee = employee.title()
        if e.get_full_name() == employee:
            e.set_salary(amount)



if __name__ == '__main__':
    employees = [
        Manager("Vera", "Schmidt", 2000),
        Waiter("Chuck", "Norris", 1800),
        Waiter("Samantha", "Carrington", 1800),
        Chef("Roberto", "Jacketti",2100),
        Mechanic("Dave", "Dressel",2200),
        Mechanic("Tina","River", 2300),
        Mechanic("Ringo", "Ramosa",1900),
        Mechanic("Chuck", "Rainey", 1800)
    ]
    print_staffing_report()
    print()
    print_account_report()
    raise_salary("Tina River", 200)
    print_account_report()

