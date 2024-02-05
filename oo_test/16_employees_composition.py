from employee import Manager, Waiter, Chef, Mechanic
from reports import AccountingReport, StaffingReport, ShiftReport
from shift import MorningShift, AfternoonShift


def raise_salary(employee, amount):
    for e in employees:
        if e.get_full_name() == employee:
            e.set_salary(amount)


if __name__ == '__main__':
    employees = [
        Manager("Vera", "Schmidt", 2000, MorningShift()),
        Waiter("Chuck", "Norris", 1800, MorningShift()),
        Waiter("Samantha", "Carrington", 1800, AfternoonShift()),
        Chef("Roberto", "Jacketti", 2100, MorningShift()),
        Mechanic("Dave", "Dressel", 2200, MorningShift()),
        Mechanic("Tina", "River", 2300, MorningShift()),
        Mechanic("Ringo", "Ramosa", 1900, MorningShift()),
        Mechanic("Chuck", "Rainey", 1800, AfternoonShift())
    ]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ShiftReport(employees)
]

for report in reports:
    report.print_report()
    print()
