from abc import abstractmethod


class DepartmentRepo:

    # @abstractmethod
    # def locate_department_by_id(self, departmentId):
    #     pass
    #
    # @abstractmethod
    # def locate_department_by_name(self, department_name):
    #     pass
    #
    # @abstractmethod
    # def locate_department_head_by_id(self, department_head_id):
    #     pass

    @abstractmethod
    def locate_request_by_id(self, employeeId):
        pass

    @abstractmethod
    def approval_status_by_supervisor(self, supervisor_name, request_status):
        pass
    