from employees import Manager, Waiter, Chef, Mechanic
import sys
sys.path.extend([r'/home/tux/PycharmProjects/pythonProject/coin_toss'])
from color import Colors

def print_account_report():
    print(f"{Colors.GREEN}Accounting")
    print(f"=========={Colors.RESET}")
    for e in employees:
        print(f"{e.name}: £{e.salary}")


def print_staffing_report():
    print(f"{Colors.GREEN}Staffing")
    print(f"=========={Colors.RESET}")
    for e in employees:
        print(f"{e.name}: {e.job_title}")
    print()

def print_path():
    from sys import path
    for p in path:
        print(p)


if __name__ == '__main__':
    employees = [
        Manager("Vera", "Smith", 2000),
        Waiter("Chuck", "Jones", 1800),
        Waiter("Samantha", "Singer", 1800),
        Chef("Roberto", "Fangio", 2100),
        Mechanic("Dave", "Tomilinson", 2200),
        Mechanic("Tina", "Arena", 2300),
        Mechanic("Ringo", "Starr", 1900)
    ]
    # print_staffing_report()
    print_account_report()
    for e in employees:
        e.salary = 100
    print_account_report()


