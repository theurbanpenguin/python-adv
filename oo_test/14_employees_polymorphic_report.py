from employee import Manager, Waiter, Chef, Mechanic
from reports import AccountingReport, StaffingReport

def raise_salary(employee, amount):
    for e in employees:
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

reports = [
    AccountingReport(employees),
    StaffingReport(employees)
]

for report in reports:
    report.print_report()
    print()