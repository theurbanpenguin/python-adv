from employee import Manager, Waiter, Chef, Mechanic
import sys, importlib
sys.path.extend(['/home/tux/PycharmProjects/pythonProject/coin_toss'])
from color import Colors


def print_account_report():
    print(f"{Colors.GREEN}Accounting")
    print(f"=========={Colors.RESET}")
    for e in employees:
        print(f"{e.name}: £{e.salary}")


def print_staffing_report():
    print(f"{colors.GREEN}Staffing")
    print(f"=========={Colors.RESET}")
    for e in employees:
        print(f"{e.name}: {e.job_title}")
    print()


if __name__ == '__main__':
    employees = [
        Manager("Vera", 2000),
        Waiter("Chuck", 1800),
        Waiter("Samantha", 1800),
        Chef("Roberto", 2100),
        Mechanic("Dave", 2200),
        Mechanic("Tina", 2300),
        Mechanic("Ringo", 1900)
    ]
    print_staffing_report()
    print_account_report()
