
from flask import request, json
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_unavailable import ResourceUnavailable
from implementations.departrepoimpl import DepartmentRepoImpl
from services.departmentservices import DepartmentServices

dr = DepartmentRepoImpl()
ds = DepartmentServices(dr)


def route(app):

    # @app.route("/department/<department_Id>", methods=["GET"])
    # def locate_department_by_id(departmentId):
    #     try:
    #         return ds.locate_department_by_id(departmentId).json(), 200
    #     except ValueError as e:
    #         return "Not a Valid ID", 400
    #     except ResourceNotFound as r:
    #         return r.message, 404
    #
    # @app.route("/department/<department_name>", methods=["GET"])
    # def locate_department_by_name(department_name):
    #     try:
    #         return ds.locate_department_by_name(department_name).json(), 200
    #     except ValueError as e:
    #         return "Incorrect Department Name", 400
    #     except ResourceNotFound as r:
    #         return r.message, 404
    #
    # @app.route("/department/<department_head_id>", methods=["GET"])
    # def locate_department_head_by_id(department_head_by_id):
    #     try:
    #         return ds.locate_department_head_by_id(department_head_by_id).json(), 200
    #     except ValueError as e:
    #         return "Department Head not Recognized", 400
    #     except ResourceNotFound as r:
    #         return r.message, 404

    @app.route("/department", methods=["GET"])
    def locate_request_by_id(employeeId):
        try:
            return ds.locate_request_by_id(employeeId).json(), 200
        except ValueError:
            return "Request cannot be Verified", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/department/<approval_status>", methods=["GET"])
    def approval_status_by_supervisor(supervisor_name, request_status):
        try:
            return ds.approval_status_by_supervisor(supervisor_name, request_status).json(), 200
        except ValueError:
            return "Request Cannot Be Completed", 400
        except ResourceUnavailable as i:
            return i.message, 404
