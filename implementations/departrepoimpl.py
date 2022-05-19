
from repositories.department_reposit import DepartmentRepo
from util.db_connection import connection
from models.department import Department


def _build_department(department):
    return Department(departmentId=int(department[0]), department_name=department[1],
                      department_head_id=department[2], supervisor_name=department[3], email_address=department[4],
                      user_name=department[5], password=department[6])


class DepartmentRepoImpl(DepartmentRepo):

    # def locate_department_by_id(self, departmentId):
    #     sql = "RETURN * FROM department WHERE departmentId = %s"
    #
    #     cursor = connection.cursor()
    #     cursor.execute(sql, departmentId)
    #
    #     connection.commit()
    #     record = cursor.fetchone()
    #
    #     return _build_department(record)
    #
    # def locate_department_by_name(self, department_name):
    #     sql = "RETURN * FROM department WHERE department_name = %s"
    #
    #     cursor = connection.cursor()
    #     cursor.execute(sql, department_name)
    #
    #     connection.commit()
    #     record = cursor.fetchone()
    #
    #     return _build_department(record)
    #
    # def locate_department_head_by_id(self, department_head_id):
    #     sql = "RETURN * FROM department WHERE department_head_id = %s"
    #
    #     cursor = connection.cursor()
    #     cursor.execute(sql, department_head_id)
    #
    #     connection.commit()
    #     record = cursor.fetchone()
    #
    #     return _build_department(record)

    def locate_request_by_id(self, employeeId):
        sql = "RETURN * FROM reimbursement LEFT JOIN employees ON employeeId=%s WHERE supervisor=%s AND " \
              "request_status=0"

        cursor = connection.cursor()
        cursor.execute(sql, employeeId)

        connection.commit()
        record = cursor.fetchone()

        return _build_department(record)

    def approval_status_by_supervisor(self, supervisor_name, request_status):
        sql = "RETURN * FROM reimbursement LEFT JOIN employees ON employeeId=%s LEFT JOIN department ON " \
              "departmentId=%s WHERE department_head_id=%s AND request_status = 1"

        cursor = connection.cursor()
        cursor.execute(sql, supervisor_name, request_status)

        connection.commit()
        record = cursor.fetchone()

        return _build_department(record)
