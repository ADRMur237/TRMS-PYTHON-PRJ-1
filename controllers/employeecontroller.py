
from flask import request, jsonify
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_unavailable import ResourceUnavailable
from models.employee import Employee
from implementations.employee_repo_impl import EmployeeRepoImpl
from services.employeeservices import EmployeeServices

er = EmployeeRepoImpl()
es = EmployeeServices(er)


def route(app):
    @app.route("/employees", methods=["POST"])
    def create_new_employee():
        body = request.json

        employee = Employee(employeeId=body["employeeId"], full_name=body["fullName"],
                            email_address=body["emailAddress"], user_name=body["username"], password=body["password"],
                            supervisor=body["supervisor"], departmentId=body["departmentId"])
        employee = es.create_new_employee(employee)

        return jsonify(employee.json(), 200)

    @app.route("/employees/<employeeId>", methods=["GET"])
    def employee_by_id(employeeId):
        try:
            return es.employee_by_id(int(employeeId)).json(), 200
        except ValueError:
            return "Not a Valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    # @app.route("/employees/<name>", methods=["GET"])
    # def employee_by_name(full_name):
    #     try:
    #         return es.employee_by_name(full_name).json(), 200
    #     except ValueError:
    #         return "Employee Name Invalid", 400
    #     except ResourceNotFound as r:
    #         return r.message, 404
    #
    # @app.route("/employees/<departmentId>", methods=["GET"])
    # def employee_by_department(departmentId):
    #     try:
    #         return es.employee_by_department(departmentId).json(), 200
    #     except ValueError:
    #         return "Department Invalid", 400
    #     except ResourceNotFound as r:
    #         return r.message, 404

    @app.route("/employees/login/", methods=["POST"])
    def employee_login(user_name, password):
        try:
            return es.employee_login(user_name, password).json(), 200
        except ValueError:
            return "Username or Password not Valid", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees/<employee_delete>", methods=["DELETE"])
    def delete_employee(employeeId):
        try:
            es.delete_employee(employeeId)
        except ResourceNotFound as r:
            return r.message, 400
        except ResourceUnavailable as i:
            return i.message(f"Employee {employeeId} not Found"), 404
        return 'Employee Information is Deleted', 204  # No Content
