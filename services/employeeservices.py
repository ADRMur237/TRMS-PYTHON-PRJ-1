
from repositories.employee_repositories import EmployeeReposit


class EmployeeServices:
    def __init__(self, employee_repositories: EmployeeReposit):
        self.employee_repositories = employee_repositories

    def create_new_employee(self, new_employee):
        return self.employee_repositories.create_new_employee(new_employee)

    def employee_by_id(self, employeeId):
        return self.employee_repositories.employee_by_id(employeeId)

    def employee_by_name(self, full_name):
        return self.employee_repositories.employee_by_name(full_name)

    def employee_by_department(self, departmentId):
        return self.employee_repositories.employee_by_department(departmentId)

    def employee_login(self, user_name, password):
        return self.employee_repositories.employee_login(user_name, password)

    def delete_employee(self, employeeId):
        return self.employee_repositories.employee_by_id(employeeId)
