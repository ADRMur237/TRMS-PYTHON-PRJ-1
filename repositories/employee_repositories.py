from abc import abstractmethod


class EmployeeReposit:

    @abstractmethod
    def create_new_employee(self, new_employee):
        pass

    @abstractmethod
    def employee_by_id(self, employeeId):
        pass

    # @abstractmethod
    # def employee_by_name(self, full_name):
    #     pass

    # @abstractmethod
    # def employee_position(self, position):
    #     pass

    # @abstractmethod
    # def employee_by_department(self, departmentId):
    #     pass

    @abstractmethod
    def employee_login(self, user_name, password):
        pass

    @abstractmethod
    def delete_employee(self, employeeId):
        pass
