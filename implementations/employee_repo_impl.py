from abc import ABC

from repositories.employee_repositories import EmployeeReposit
from util.db_connection import connection
from models.employee import Employee


def _build_employee(employees):
    return Employee(employeeId=int(employees[0]), full_name=employees[1],
                    email_address=employees[2], user_name=employees[3], password=employees[4],
                    supervisor=employees[5], departmentId=employees[6])


class EmployeeRepoImpl(EmployeeReposit, ABC):
    def create_new_employee(self, new_employee):
        sql = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
        employee_properties = [new_employee.employeeId, new_employee.full_name,
                               new_employee.email_address, new_employee.user_name,
                               new_employee.password, new_employee.supervisor, new_employee.departmentId]

        cursor = connection.cursor()

        cursor.execute(sql, employee_properties)

        connection.commit()
        record = cursor.fetchone()

        return _build_employee(record)

    def employee_by_id(self, employeeId):
        sql = "SELECT * FROM employees WHERE employeeId = %s"

        cursor = connection.cursor()
        cursor.execute(sql, employeeId)

        connection.commit()
        record = cursor.fetchone()

        return _build_employee(record)

    # def employee_by_name(self, full_name):
    #     sql = "SELECT * FROM employees WHERE full_name = %s"
    #
    #     cursor = connection.cursor()
    #     cursor.execute(sql, full_name)
    #
    #     connection.commit()
    #     records = cursor.fetchall()
    #
    #     return [_build_employee(record) for record in records]

    # def employee_position(self, position):
    #     sql = "SELECT * FROM employees WHERE employee_position = %s"
    #
    #     cursor = connection.cursor()
    #     cursor.execute(sql, position)
    #
    #     record = cursor.fetchone()
    #
    #     return _build_employee(record)

    # def employee_by_department(self, departmentId):
    #     sql = "SELECT * FROM employees WHERE departmentId = %s"
    #     cursor = connection.cursor()
    #     cursor.execute(sql, departmentId)
    #
    #     connection.commit()
    #     record = cursor.fetchone()
    #
    #     return _build_employee(record)

    def employee_login(self, user_name, password):
        sql = "SELECT * FROM employees WHERE user_name = %s, password = %s"

        cursor = connection.cursor()
        cursor.execute(sql, user_name, password)

        connection.commit()
        record = cursor.fetchall()

        return _build_employee(record)

    def delete_employee(self, employeeId):
        sql = "DELETE FROM employees WHERE employeeId = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, employeeId)

        connection.commit()
        record = cursor.fetchone()

        return _build_employee(record)
