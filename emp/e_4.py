from employees import Manager, Waiter, Chef, Mechanic

def print_accounting_report():
    print("Accounting")
    print("++++++++++")
    for e in employees:
        print(f'{e.name}: {e.salary}')
    print()
def print_staffing_report():
    print("Staffing")
    print("++++++++")
    for e in employees:
        print(f'{e.name}: {e.job_title}')
    print()
if __name__ == '__main__':
    employees: list = [
        Manager("Vera", 2000),
        Waiter("Chuck", 1800),
        Waiter("Samantha", 1800),
        Chef("Roberto", 2100),
        Mechanic("Dave", 2200),
        Mechanic("Tina", 2300),
        Mechanic("Ringo", 1900),
    ]
print_accounting_report()
print_staffing_report()