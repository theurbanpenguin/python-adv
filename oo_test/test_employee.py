import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_get_full_name(self):
        e = Employee("Ted", "Baker", 0)
        self.assertEqual(e.get_full_name(), "Ted Baker")

    def test_raise_salary(self):
        e = Employee("","", 2000)
        e.raise_salary(100)
        self.assertEqual(e.salary, 2100)