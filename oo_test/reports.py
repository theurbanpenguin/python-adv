class Report:
    def __init__(self, emp_list):
        self._emp_list = emp_list
class AccountingReport(Report):
    def print_report(self):
        print("Accounting")
        print("==========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}: £{e.get_salary()}")
class StaffingReport(Report):
    def print_report(self):
        print("Staffing")
        print("==========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}: {e.job_title}")

class ShiftReport(Report):
    def print_report(self):
        print("Shift")
        print("==========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}: {e.shift.get_shift_info()}")