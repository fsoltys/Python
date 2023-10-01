import unittest
from employees import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Jakub", "Przykladowy", 124500)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 126500)

    def test_give_custom_raise(self):
        self.employee.give_raise(5000)
        self.assertEqual(self.employee.annual_salary, 129500)


if __name__ == "__main__":
    unittest.main()
