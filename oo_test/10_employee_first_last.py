from employee import Manager
from employee import Waiter
from employee import Chef
from employee import Mechanic

def print_account_report():
    print("Accounting")
    print("==========")
    for e in employees:
        print(f"{e.first_name} {e.last_name}: £{e.salary}")

def print_staffing_report():
    print("Staffing")
    print("==========")
    for e in employees:
        print(f"{e.first_name} {e.last_name}: {e.job_title}")



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

