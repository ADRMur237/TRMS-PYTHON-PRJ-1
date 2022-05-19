from repositories.department_reposit import DepartmentRepo


class DepartmentServices:

    def __init__(self, department_reposit: DepartmentRepo):
        self.department_reposit = department_reposit

    # def locate_department_by_id(self, departmentId):
    #     return self.department_reposit.locate_department_by_id(departmentId)
    #
    # def locate_department_by_name(self, department_name):
    #     return self.department_reposit.locate_department_by_name(department_name)
    #
    # def locate_department_head_by_id(self, department_head_id):
    #     return self.department_reposit.locate_department_head_by_id(department_head_id)

    def locate_request_by_id(self, employeeId):
        return self.department_reposit.locate_request_by_id(employeeId)

    def approval_status_by_supervisor(self, supervisor_name, request_status):
        return self.department_reposit.approval_status_by_supervisor(supervisor_name, request_status)
