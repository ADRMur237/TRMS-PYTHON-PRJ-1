
from flask import jsonify
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_unavailable import ResourceUnavailable
from models.reimbursement import Reimbursement
from implementations.reimburserepoimpl import ReimburseRepoImpl
from services.reimburservices import ReimburseService

rr = ReimburseRepoImpl()
rs = ReimburseService(rr)


def route(app):

    @app.route("/request", methods=["POST"])
    def create_request(request):
        body = request.json

        request = Reimbursement(requestId=body["requestId"], employeeId=body["employeeId"], event_cost=body["eventCost"],
                                event_reimbursement=body["eventReimbursement"], employee_grade=body["eventGrade"],
                                request_status=body["requestStatus"])
        request = rs.create_request(request)

        return jsonify(request.json(), 200)

    @app.route("/request/<request_id>", methods=["GET"])
    def request_by_id(requestId):
        try:
            return rs.request_by_Id(int(requestId)).json(), 200
        except ValueError:
            return "Not a Valid Request ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/request/<employeeId>", methods=['GET'])
    def employee_request(employeeId):
        try:
            return rs.employee_request(int(employeeId)).json(), 200
        except ValueError:
            return "Request Cannot be Completed", 400
        except ResourceNotFound as r:
            return r.message, 404

    # @app.route("/request/<amount>", methods=['GET'])
    # def amount_cost(event_cost):
    #     try:
    #         return rs.amount_cost(event_cost).json(), 200
    #     except ValueError:
    #         return "Amount is not Verified", 400
    #     except ResourceUnavailable as i:
    #         return i.message, 404

    @app.route("/request/<reimbursement>", methods=['GET'])
    def request_reimbursement(event_reimbursement):
        try:
            return rs.request_reimbursement(event_reimbursement).json(), 200
        except ValueError:
            return "Request Cannot Be Completed", 400
        except ResourceUnavailable as i:
            return i.message, 404

    @app.route("/request/<grade_status>", methods=['GET'])
    def update_grade_status(employee_grade):
        try:
            return rs.update_grade_status(employee_grade).json(), 200
        except ValueError:
            return "Status cannot be confirmed", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/request/<approval>", methods=['GET'])
    def approval_status(request_status):
        try:
            return rs.approval_status(request_status).json(), 200
        except ResourceUnavailable as i:
            return i.message, 400
        except ResourceNotFound as r:
            return r.message, 404
