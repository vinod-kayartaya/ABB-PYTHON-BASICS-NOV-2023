class IdError(Exception):
    def __init__(self, message='Invalid value for id'):
        super().__init__(message)


class EmpNameError(Exception):
    def __init__(self, message='Invalid value for employee name'):
        super().__init__(message)


class SalaryError(Exception):
    def __init__(self, message='Invalid value for employee salary'):
        super().__init__(message)

