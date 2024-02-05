from employee import Manager, Waiter, Chef, Mechanic
from reports import AccountingReport, StaffingReport, ShiftReport
from datetime import time


def raise_salary(employee, amount):
    for e in employees:
        if e.get_full_name() == employee:
            e.set_salary(amount)


if __name__ == '__main__':
    employees = [
        Manager("Vera", "Schmidt", 2000, time(8, 00), time(14, 00)),
        Waiter("Chuck", "Norris", 1800, time(8, 00), time(14, 00)),
        Waiter("Samantha", "Carrington", 1800, time(12, 00), time(20, 00)),
        Chef("Roberto", "Jacketti", 2100, time(8, 00), time(14, 00)),
        Mechanic("Dave", "Dressel", 2200, time(8, 00), time(14, 00)),
        Mechanic("Tina", "River", 2300, time(8, 00), time(14, 00)),
        Mechanic("Ringo", "Ramosa", 1900, time(8, 00), time(14, 00)),
        Mechanic("Chuck", "Rainey", 1800, time(12, 00), time(20, 00))
    ]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ShiftReport(employees)
]

for report in reports:
    report.print_report()
    print()
