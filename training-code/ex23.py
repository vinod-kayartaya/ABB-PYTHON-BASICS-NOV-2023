from emp_exceptions import *


class Employee:
    def __init__(self, **kwargs):
        emp_id = kwargs.get('emp_id')
        if emp_id is not None and type(emp_id) is not int:
            raise IdError('employee id must be an int')
        self.emp_id = emp_id

        emp_name = kwargs.get('emp_name')
        if emp_name is not None and type(emp_name) is not str:
            raise EmpNameError('employee name must be a str')
        if emp_name is not None and emp_name.strip() == '':
            raise EmpNameError('employee name cannot be blank')

        self.emp_name = emp_name

        salary = kwargs.get('salary')
        if salary is not None and type(salary) not in (int, float):
            raise SalaryError('salary must be one of `int` or `float`')
        if salary is not None and (salary < 15000 or salary > 200000):
            raise SalaryError('salary must be between 15000 and 200000')

        self.salary = salary

    def __str__(self):
        ename = None if self.emp_name is None else f'"{self.emp_name}"'
        return f'Employee(emp_id={self.emp_id}, emp_name={ename}, salary={self.salary})'


def main():
    e1 = Employee(emp_id=13421, salary=20000)
    print(e1)


if __name__ == '__main__':
    main()
